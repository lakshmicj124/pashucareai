"""Pydantic models for user authentication."""

from pydantic import BaseModel


from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    phone_number: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    phone_number: Optional[str] = None


class TokenResponse(BaseModel):
    token: str
    user: UserResponse


class UserUpdate(BaseModel):
    name: str
    email: str
    phone_number: str


class PasswordUpdate(BaseModel):
    current_password: str
    new_password: str
