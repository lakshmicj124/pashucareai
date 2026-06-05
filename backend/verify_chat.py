import asyncio
import sys
sys.path.append(r"c:\Users\DELL\Documents\cow disease project\backend")

from app.routes.chat import chat_with_ai, ChatRequest, Message
from app.database import connect_db

async def test_chat():
    print("Testing AI assistant chat routes and fallbacks...")
    await connect_db()
    
    # 1. Test greeting in Hindi
    req_greeting_hi = ChatRequest(
        messages=[Message(role="user", text="नमस्ते")],
        lang="hi"
    )
    mock_user = {"_id": "6a1c4da75d1e14b7a72b2966"}
    res = await chat_with_ai(req_greeting_hi, user=mock_user)
    print(f"\nGreeting (HI) response:\n{ascii(res['response'])}")

    # 2. Test off-topic in Kannada
    req_off_topic = ChatRequest(
        messages=[Message(role="user", text="Write a python program to print hello world")],
        lang="kn"
    )
    res = await chat_with_ai(req_off_topic, user=mock_user)
    print(f"\nOff-topic (KN) response:\n{ascii(res['response'])}")

    # 3. Test specific disease (Jaw Swelling) in English
    req_disease = ChatRequest(
        messages=[Message(role="user", text="Tell me about Jaw Swelling in goats")],
        lang="en"
    )
    res = await chat_with_ai(req_disease, user=mock_user)
    print(f"\nDisease (EN) response:\n{ascii(res['response'])}")

if __name__ == "__main__":
    asyncio.run(test_chat())
