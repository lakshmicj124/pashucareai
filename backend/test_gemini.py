import asyncio
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

async def test():
    key = os.getenv("GEMINI_API_KEY")
    print(f"Key from env: {key}")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    payload = {
        "contents": [{"role": "user", "parts": [{"text": "Hello, are you there?"}]}]
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.post(url, json=payload)
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            print(f"Response Body: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
