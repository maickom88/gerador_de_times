from typing import List
from fastapi import APIRouter

from src.settings.logger import logger

router = APIRouter()
draw_router = {
    "router": router,
    "prefix": "/draw",
    "tags": ["Draw"],
}


@router.get(path="", response_model=List[DrawOutput])
async def get_draws():
    logger.info("Starting request to get_draws")
    service = DrawService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=DrawOutput)
async def get_draw(guid: str):
    logger.info("Starting request to get_draw")
    service = DrawService()
    return await service.get_entity_by_guid(guid)


@router.post(path="", response_model=DrawOutput, status_code=201)
async def register_draw(draw: DrawInput):
    logger.info("Starting request to register_draw")
    service = DrawService()
    return await service.create(draw)


@router.put(path="", response_model=DrawOutput, status_code=201)
async def update_draw(draw: DrawInput):
    logger.info("Starting request to update_draw")
    service = DrawService()
    return await service.update(draw)


@router.delete(path="/{guid}", status_code=204)
async def delete_draw(guid: str):
    logger.info("Starting request to delete_draw")
    service = DrawService()
    return await service.delete_entity(guid)
