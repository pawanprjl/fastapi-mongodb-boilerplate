from pydantic import BaseModel
from uuid import UUID


class UserBase(BaseModel):
    fullname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    is_active: bool

