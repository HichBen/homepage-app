from .models import HomePage, HomePageIn
from .db import homepage, database


async def add_homepage(payload: HomePageIn):
    query = homepage.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_homepage(id):
    query = homepage.select(homepage.c.group_id == id)
    return await database.fetch_one(query=query)


async def delete_homepage(id: int):
    query = homepage.delete().where(homepage.c.group_id == id)
    return await database.execute(query=query)


async def update_homepage(id: int, payload: HomePage):
    query = (
        homepage
            .update()
            .where(homepage.c.group_id == id)
            .values(**payload.dict())
    )
    return await database.execute(query=query)


async def get_all_homepages():
    query = homepage.select()
    return await database.fetch_all(query=query)