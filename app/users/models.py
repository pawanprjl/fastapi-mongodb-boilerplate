from beanie import Document
from uuid import UUID, uuid4
from pydantic import Field


class User(Document):
    id: UUID = Field(default_factory=uuid4)
    fullname: str
    email: str
    password: str
    is_active: bool = Field(default=True)

    class Settings:
        name = "users"
