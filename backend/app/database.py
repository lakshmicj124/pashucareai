"""MongoDB connection management with an automatic local in-memory fallback database."""

import uuid
import json
import os
from datetime import datetime, timezone
from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
from bson import ObjectId

DB_FILE = "mock_database.json"

# --- Mock Database Fallback Classes ---
class MockCursor:
    def __init__(self, data):
        self.data = data

    def sort(self, *args, **kwargs):
        # Sort by timestamp desc if applicable
        try:
            self.data = sorted(
                self.data,
                key=lambda x: x.get("timestamp", ""),
                reverse=True
            )
        except Exception:
            pass
        return self

    def limit(self, limit_num):
        self.data = self.data[:limit_num]
        return self

    def __aiter__(self):
        self.index = 0
        return self

    async def __anext__(self):
        if self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            return val
        else:
            raise StopAsyncIteration


class MockCollection:
    def __init__(self, name):
        self.name = name
        self.documents = []
        self._load()

    def _load(self):
        if os.path.exists(DB_FILE):
            try:
                with open(DB_FILE, "r") as f:
                    data = json.load(f)
                    self.documents = data.get(self.name, [])
            except Exception:
                pass

    def _save(self):
        data = {}
        if os.path.exists(DB_FILE):
            try:
                with open(DB_FILE, "r") as f:
                    data = json.load(f)
            except Exception:
                pass
        data[self.name] = self.documents
        try:
            with open(DB_FILE, "w") as f:
                json.dump(data, f)
        except Exception:
            pass

    async def find_one(self, query):
        for doc in self.documents:
            match = True
            for k, v in query.items():
                # Handle ObjectId query matching
                if k == "_id":
                    doc_id = str(doc.get("_id"))
                    query_id = str(v)
                    if doc_id != query_id:
                        match = False
                elif doc.get(k) != v:
                    match = False
            if match:
                # Return copy so caller doesn't mutate db state directly
                return dict(doc)
        return None

    async def insert_one(self, doc):
        doc = dict(doc)
        if "_id" not in doc:
            doc["_id"] = str(ObjectId())  # Store as string for JSON serialization
        elif isinstance(doc["_id"], ObjectId):
            doc["_id"] = str(doc["_id"])
            
        self.documents.append(doc)
        self._save()
        
        class InsertResult:
            def __init__(self, inserted_id):
                self.inserted_id = inserted_id
        return InsertResult(doc["_id"])

    def find(self, query=None):
        query = query or {}
        results = []
        for doc in self.documents:
            match = True
            for k, v in query.items():
                if doc.get(k) != v:
                    match = False
            if match:
                results.append(dict(doc))
        return MockCursor(results)

    async def count_documents(self, query=None):
        query = query or {}
        count = 0
        for doc in self.documents:
            match = True
            for k, v in query.items():
                if doc.get(k) != v:
                    match = False
            if match:
                count += 1
        return count

    async def delete_one(self, query):
        for idx, doc in enumerate(self.documents):
            match = True
            for k, v in query.items():
                if k == "_id":
                    doc_id = str(doc.get("_id"))
                    query_id = str(v)
                    if doc_id != query_id:
                        match = False
                elif doc.get(k) != v:
                    match = False
            if match:
                self.documents.pop(idx)
                self._save()
                class DeleteResult:
                    def __init__(self, deleted_count):
                        self.deleted_count = deleted_count
                return DeleteResult(1)
        class DeleteResult:
            def __init__(self, deleted_count):
                self.deleted_count = deleted_count
        return DeleteResult(0)

    async def delete_many(self, query):
        initial_count = len(self.documents)
        new_docs = []
        deleted_count = 0
        for doc in self.documents:
            match = True
            for k, v in query.items():
                if k == "_id":
                    doc_id = str(doc.get("_id"))
                    query_id = str(v)
                    if doc_id != query_id:
                        match = False
                elif doc.get(k) != v:
                    match = False
            if match:
                deleted_count += 1
            else:
                new_docs.append(doc)
        self.documents = new_docs
        self._save()
        class DeleteResult:
            def __init__(self, deleted_count):
                self.deleted_count = deleted_count
        return DeleteResult(deleted_count)

    async def create_index(self, *args, **kwargs):
        pass


class MockDatabase:
    def __init__(self):
        self.users = MockCollection("users")
        self.detections = MockCollection("detections")
        self.chat_sessions = MockCollection("chat_sessions")
        self.chat_messages = MockCollection("chat_messages")
        print("[INFO] PashuCare Mock Database Initialized (In-Memory Fallback)")


# --- Global connection state ---
client: AsyncIOMotorClient = None
db = None


async def connect_db():
    """Establish connection to MongoDB or fall back to MockDatabase."""
    global client, db
    uri = settings.MONGODB_URI
    if not uri:
        print("[WARN] MONGODB_URI not found. Falling back to MockDatabase.")
        db = MockDatabase()
        return

    try:
        # Hide password in logs
        log_uri = uri.split("@")[-1] if "@" in uri else uri
        print(f"[INFO] Connecting to MongoDB: {log_uri}")
        client = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=3000)
        # Verify connection by pinging
        await client.admin.command('ping')
        db = client[settings.DATABASE_NAME]
        print(f"[INFO] Successfully connected to MongoDB Atlas database: {settings.DATABASE_NAME}")
    except Exception as e:
        print(f"[WARN] Failed to connect to MongoDB ({e}). Falling back to MockDatabase.")
        client = None
        db = MockDatabase()


async def close_db():
    """Close MongoDB connection."""
    global client
    if client:
        client.close()


def get_db():
    """Return the database instance."""
    return db
