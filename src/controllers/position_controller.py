from typing import List
from fastapi import APIRouter

from src.models.position_model import PositionOutput, PositionInput
from src.services.position_service import PositionService
from src.settings.logger import logger

router = APIRouter()
position_router = {
    "router": router,
    "prefix": "/position",
    "tags": ["Position"],
}


@router.get(path="", response_model=List[PositionOutput])
async def get_position():
    logger.info("Starting request to get_position")
    service = PositionService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=PositionOutput)
async def get_position(guid: str):
    logger.info("Starting request to get_position")
    service = PositionService()
    return await service.get_entity_by_guid(guid)


@router.post(path="", response_model=PositionOutput, status_code=201)
async def register_position(position: PositionInput):
    logger.info("Starting request to register_position")
    service = PositionService()
    return await service.create(position)


@router.put(path="", response_model=PositionOutput, status_code=201)
async def update_position(position: PositionInput):
    logger.info("Starting request to update_position")
    service = PositionService()
    return await service.update(position)


@router.delete(path="/{guid}", status_code=204)
async def delete_position(guid: str):
    logger.info("Starting request to delete_position")
    service = PositionService()
    return await service.delete_entity(guid)
