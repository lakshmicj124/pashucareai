import asyncio
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import pymongo

# Load environment variables
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "pashucare_ai")

async def create_collections():
    print(f"Connecting to MongoDB at: {MONGODB_URI.split('@')[-1] if '@' in MONGODB_URI else MONGODB_URI}")
    client = AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    db = client[DATABASE_NAME]

    try:
        # Verify connection
        print("Pinging MongoDB Atlas...")
        await client.admin.command('ping')
        print("Successfully pinged MongoDB.")
        
        print("Checking/creating collections...")
        # 1. Chat Sessions Collection
        sessions_col = db["chat_sessions"]
        print("Creating indexes on 'chat_sessions'...")
        await sessions_col.create_index("user_id")
        await sessions_col.create_index([("updated_at", -1)])
        print("Indexes created for 'chat_sessions'.")

        # 2. Chat Messages Collection
        messages_col = db["chat_messages"]
        print("Creating indexes on 'chat_messages'...")
        await messages_col.create_index("session_id")
        await messages_col.create_index("user_id")
        await messages_col.create_index([("timestamp", 1)])
        print("Indexes created for 'chat_messages'.")

        print("\nDatabase initialization complete! Collections 'chat_sessions', 'chat_messages', and 'users' are ready with indexes.")
        # 3. Users Collection for registration and login
        users_col = db["users"]
        print("Creating indexes on 'users' collection for authentication...")
        # Unique index on email
        await users_col.create_index("email", unique=True)
        # Index on username for quick lookup (optional)
        await users_col.create_index("username")
        # Index on created_at for sorting
        await users_col.create_index([("created_at", -1)])
        print("Indexes created for 'users' collection.")
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print(f"\n[WARN] Could not connect to MongoDB Atlas ({e}).")
        print("[WARN] Local fallback MockDatabase will be used for session storage instead.")
        print("[WARN] The application is still fully functional using mock_database.json!")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(create_collections())
