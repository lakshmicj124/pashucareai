import os
from pathlib import Path
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

load_dotenv(Path('.env'))
uri = os.getenv('MONGODB_URI')

async def test():
    try:
        client = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=5000)
        await client.admin.command('ping')
        print('[OK] MongoDB connection successful')
    except Exception as e:
        print('[ERROR] MongoDB connection failed:', e)


if __name__ == '__main__':
    asyncio.run(test())
