from typing import List
from fastapi import APIRouter

from src.models.sport_model import SportOutput, SportInput
from src.services.sport_service import SportService
from src.settings.logger import logger

router = APIRouter()
sport_router = {
    "router": router,
    "prefix": "/sport",
    "tags": ["Sport"],
}


@router.get(path="", response_model=List[SportOutput])
async def get_sports():
    logger.info("Starting request to get_sports")
    service = SportService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=SportOutput)
async def get_sport(guid: str):
    logger.info("Starting request to get_sport")
    service = SportService()
    return await service.get_entity_by_guid(guid)


@router.post(path="", response_model=SportOutput, status_code=201)
async def register_sport(sport: SportInput):
    logger.info("Starting request to register_sport")
    service = SportService()
    return await service.create(sport)


@router.put(path="", response_model=SportOutput, status_code=201)
async def update_sport(sport: SportInput):
    logger.info("Starting request to update_sport")
    service = SportService()
    return await service.update(sport)


@router.delete(path="/{guid}", status_code=204)
async def delete_sport(guid: str):
    logger.info("Starting request to delete_sport")
    service = SportService()
    return await service.delete_entity(guid)
