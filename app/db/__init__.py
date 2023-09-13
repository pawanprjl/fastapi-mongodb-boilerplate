from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.config import settings
import app.db.models as models


async def init_db():
    client = AsyncIOMotorClient(settings.MONGO_DB_URL)
    await init_beanie(
        database=client.get_default_database(),
        document_models=models.__all__
    )
