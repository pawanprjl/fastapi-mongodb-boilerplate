import os
import dotenv
from functools import lru_cache


class BaseConfig:
    # load environment variable
    dotenv.load_dotenv()

    # fetch database config from .env
    DB_PROVIDER = os.environ.get("DB_PROVIDER", "mongodb")
    DB_DATABASE = os.environ.get("DB_DATABASE", "mongo-fastapi")
    DB_USER = os.environ.get("DB_USER", "admin")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "27017")

    MONGO_DB_URL = f"{DB_PROVIDER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:27017/{DB_DATABASE}?authSource=admin"


class DevelopmentConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dist = {
        "dev": DevelopmentConfig,
        "prod": ProdConfig
    }

    config_name = os.environ.get("FAST_API_CONFIG", "dev")
    config_cls = config_cls_dist[config_name]
    return config_cls


settings = get_settings()
