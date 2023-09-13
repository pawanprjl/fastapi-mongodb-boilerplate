from fastapi import APIRouter, Body
from typing import List

from . import crud, models, schemas

router = APIRouter(
    prefix="/user"
)


@router.get("/", response_model=List[schemas.User])
async def get_all_users():
    users = await crud.get_all_users()
    return users


@router.post("/create/")
async def create_user(user: schemas.UserCreate = Body(...)):
    new_user = await crud.create_user(user)
    return new_user
