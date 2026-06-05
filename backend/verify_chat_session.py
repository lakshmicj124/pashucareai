import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import connect_db, get_db
from app.routes.chat import chat_with_ai, ChatRequest, Message, get_sessions, get_messages, delete_chat_session

async def test_session_lifecycle():
    print("Initializing Database...")
    await connect_db()
    db = get_db()
    
    # Clean previous test entries
    if hasattr(db.chat_sessions, "delete_many"):
        await db.chat_sessions.delete_many({"user_id": "test_user_123"})
        await db.chat_messages.delete_many({"user_id": "test_user_123"})

    dummy_user = {"_id": "test_user_123", "email": "test@example.com"}

    print("\n--- 1. Testing Chat Session Creation on first text message ---")
    req = ChatRequest(
        message="लम्पी त्वचा रोग क्या है?",  # Lumpy skin disease in Hindi
        lang="hi"
    )
    res = await chat_with_ai(req, user=dummy_user)
    print("Response payload:")
    print(ascii(res))
    session_id = res.get("session_id")
    assert session_id is not None, "session_id should be returned"
    
    print("\n--- 2. Testing Message Continuation with context ---")
    req2 = ChatRequest(
        session_id=session_id,
        message="इसके लक्षण क्या हैं?",  # "What are its symptoms?" in Hindi (refers back to Lumpy skin context!)
        lang="hi"
    )
    res2 = await chat_with_ai(req2, user=dummy_user)
    print("Continuation response payload:")
    print(ascii(res2))

    print("\n--- 3. Testing Sessions Listing ---")
    sessions = await get_sessions(user=dummy_user)
    print(f"User sessions count: {len(sessions)}")
    print(ascii(sessions))
    assert len(sessions) > 0, "Should have at least 1 session"

    print("\n--- 4. Testing Session Message Retrieval ---")
    messages = await get_messages(session_id, user=dummy_user)
    print(f"Session messages count: {len(messages)}")
    for msg in messages:
        print(f"  [{msg.get('role')}]: {ascii(msg.get('text'))} (EN: {ascii(msg.get('text_en'))})")
    assert len(messages) >= 4, "Should have at least 4 messages (2 turns: user, assistant, user, assistant)"

    print("\n--- 5. Testing Duplicate Message Prevention ---")
    # Send the exact same message again immediately
    req_dup = ChatRequest(
        session_id=session_id,
        message="इसके लक्षण क्या हैं?",
        lang="hi"
    )
    # The duplicate check should match and return within 3 seconds
    import time
    start = time.time()
    res_dup = await chat_with_ai(req_dup, user=dummy_user)
    end = time.time()
    print(f"Duplicate call returned in {end - start:.4f} seconds")
    print("Duplicate response text snippet:", ascii(res_dup.get("response")[:60]))

    print("\n--- 6. Testing Session Deletion ---")
    del_res = await delete_chat_session(session_id, user=dummy_user)
    print("Deletion response:", del_res)
    
    sessions_after = await get_sessions(user=dummy_user)
    print(f"User sessions count after delete: {len(sessions_after)}")
    assert len(sessions_after) == 0, "Sessions should be empty after deletion"

    print("\nSession Lifecycle Tests Completed Successfully!")

if __name__ == "__main__":
    asyncio.run(test_session_lifecycle())
