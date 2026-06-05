"""Authentication routes — register, login, and get current user."""

from datetime import datetime, timezone
import re
from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId

from ..models.user import UserCreate, UserLogin, UserResponse, TokenResponse, UserUpdate, PasswordUpdate
from ..services.auth_service import hash_password, verify_password, create_token
from ..middleware.auth import get_current_user
from ..database import get_db

router = APIRouter(prefix="/api/auth", tags=["Authentication"])


@router.post("/register", response_model=TokenResponse)
async def register(data: UserCreate):
    """Register a new user account."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database not available. Check MongoDB connection.")

    # Validate email format
    email_clean = data.email.lower().strip()
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email_clean):
        raise HTTPException(status_code=400, detail="Invalid email format.")

    # Validate phone format (+91 XXXXXXXXXX or 10 digits)
    phone_clean = data.phone_number.strip()
    if not re.match(r'^(\+91[\-\s]?)?[0-9]{10}$', phone_clean):
        raise HTTPException(status_code=400, detail="Invalid phone format. Please enter a valid 10-digit number or prefix with +91.")

    # Check if email already exists
    existing = await db.users.find_one({"email": email_clean})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check if phone already exists
    existing_phone = await db.users.find_one({"phone_number": phone_clean})
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    # Validate password requirements
    if len(data.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_]', data.password):
        raise HTTPException(status_code=400, detail="Password must include at least one special character.")

    # Create user document
    user_doc = {
        "name": data.name.strip(),
        "email": email_clean,
        "phone_number": phone_clean,
        "password": hash_password(data.password),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    result = await db.users.insert_one(user_doc)
    user_id = str(result.inserted_id)

    token = create_token(user_id)
    return TokenResponse(
        token=token,
        user=UserResponse(
            id=user_id, 
            name=user_doc["name"], 
            email=user_doc["email"], 
            phone_number=user_doc.get("phone_number")
        ),
    )


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin):
    """Login with email and password."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database not available. Check MongoDB connection.")

    user = await db.users.find_one({"email": data.email.lower().strip()})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    user_id = str(user["_id"])
    token = create_token(user_id)
    return TokenResponse(
        token=token,
        user=UserResponse(
            id=user_id, 
            name=user["name"], 
            email=user["email"], 
            phone_number=user.get("phone_number")
        ),
    )


@router.get("/me", response_model=UserResponse)
async def get_me(user=Depends(get_current_user)):
    """Get the currently authenticated user."""
    return UserResponse(
        id=str(user["_id"]),
        name=user["name"],
        email=user["email"],
        phone_number=user.get("phone_number"),
    )


@router.put("/profile", response_model=UserResponse)
async def update_profile(data: UserUpdate, user=Depends(get_current_user)):
    """Update profile information."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database not available. Check MongoDB connection.")

    # Validate email format
    email_clean = data.email.lower().strip()
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email_clean):
        raise HTTPException(status_code=400, detail="Invalid email format.")

    # Validate phone format
    phone_clean = data.phone_number.strip()
    if not re.match(r'^(\+91[\-\s]?)?[0-9]{10}$', phone_clean):
        raise HTTPException(status_code=400, detail="Invalid phone format. Please enter a valid 10-digit number.")

    # Check email duplicate
    email_owner = await db.users.find_one({"email": email_clean})
    if email_owner and str(email_owner["_id"]) != str(user["_id"]):
        raise HTTPException(status_code=400, detail="Email already taken by another account.")

    # Check phone duplicate
    phone_owner = await db.users.find_one({"phone_number": phone_clean})
    if phone_owner and str(phone_owner["_id"]) != str(user["_id"]):
        raise HTTPException(status_code=400, detail="Phone number already taken by another account.")

    # Update document
    await db.users.update_one(
        {"_id": user["_id"]},
        {"$set": {
            "name": data.name.strip(),
            "email": email_clean,
            "phone_number": phone_clean
        }}
    )

    return UserResponse(
        id=str(user["_id"]),
        name=data.name.strip(),
        email=email_clean,
        phone_number=phone_clean,
    )


@router.put("/password")
async def update_password(data: PasswordUpdate, user=Depends(get_current_user)):
    """Update password."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database not available. Check MongoDB connection.")

    # Verify old password
    if not verify_password(data.current_password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect current password.")

    # Validate new password
    if len(data.new_password) < 8:
        raise HTTPException(status_code=400, detail="New password must be at least 8 characters.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_]', data.new_password):
        raise HTTPException(status_code=400, detail="New password must include at least one special character.")

    # Hash and save
    await db.users.update_one(
        {"_id": user["_id"]},
        {"$set": {"password": hash_password(data.new_password)}}
    )

    return {"message": "Password changed successfully."}

