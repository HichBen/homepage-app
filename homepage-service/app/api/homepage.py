from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from .models import HomePageIn, HomePage, HomePageOut, HomePageUpdate
from ..api import db_manager

homepage = APIRouter()


@homepage.post('/', response_model=HomePageOut, status_code=201)
async def add_homepage(payload: HomePageIn):
    group_id = await db_manager.add_homepage(payload)
    response = {
        'group_id': group_id,
        **payload.dict()
    }
    return response


@homepage.get('/{id}/', response_model=HomePage)
async def get_homepage(id: int):
    homep = await db_manager.get_homepage(id)
    if not homep:
        raise HTTPException(status_code=404, detail="Homepage not found")
    return homep


@homepage.patch('/{id}/', response_model=HomePageUpdate)
async def update_homepage(id: int, payload: HomePageUpdate):
    stored_hp_data = await db_manager.get_homepage(id)
    if not stored_hp_data:
        raise HTTPException(status_code=404, detail="Homepage not found")

    stored_hp_model = HomePageIn(**stored_hp_data)

    update_data = payload.dict(exclude_unset=True)

    updated_homepage = stored_hp_model.copy(update=update_data)
    await db_manager.update_homepage(id, updated_homepage)
    return jsonable_encoder(updated_homepage)


@homepage.delete('/{id}/', response_model=None)
async def delete_homepage(id: int):
    homep = await db_manager.get_homepage(id)
    if not homep:
        raise HTTPException(status_code=404, detail="group not found")
    return await db_manager.delete_homepage(id)


@homepage.get('/')
async def get_homepages():
    return await db_manager.get_all_homepages()
