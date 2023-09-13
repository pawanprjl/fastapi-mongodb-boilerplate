from fastapi import FastAPI

from app.db import init_db


def create_app() -> FastAPI:
    app = FastAPI()

    # routes section here
    from app.users import router as users_router
    app.include_router(users_router, tags=["User Router"])

    @app.get("/", tags=["Root"])
    async def root():
        return {"message": "Welcome to FastAPI."}

    @app.on_event("startup")
    async def start_database():
        await init_db()

    return app
