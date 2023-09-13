from typing import List

from . import models, schemas

user_collection = models.User


async def get_all_users() -> List[models.User]:
    users = await user_collection.all().to_list()
    return users


async def create_user(new_user: schemas.UserCreate) -> models.User:
    fake_hashed_password = new_user.password + "notreallyhashed"

    db_user = models.User(
        fullname=new_user.fullname,
        email=new_user.email,
        password=fake_hashed_password
    )

    user = await db_user.create()
    return user
