from typing import List
from fastapi import APIRouter

from src.models.cup_model import CupOutput, CupInput
from src.services.cup_service import CupService
from src.settings.logger import logger

router = APIRouter()
cup_router = {
    "router": router,
    "prefix": "/cup",
    "tags": ["Cup"],
}


@router.get(path="", response_model=List[CupOutput])
async def get_cups():
    logger.info("Starting request to get_cups")
    service = CupService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=CupOutput)
async def get_cup(guid: str):
    logger.info("Starting request to get_cup")
    service = CupService()
    return await service.get_entity_by_guid(guid)


@router.post(path="", response_model=CupOutput, status_code=201)
async def register_cup(cup: CupInput):
    logger.info("Starting request to register_cup")
    service = CupService()
    return await service.create(cup)


@router.put(path="", response_model=CupOutput, status_code=201)
async def update_cup(cup: CupInput):
    logger.info("Starting request to update_cup")
    service = CupService()
    return await service.update(cup)


@router.delete(path="/{guid}", status_code=204)
async def delete_cup(guid: str):
    logger.info("Starting request to delete_cup")
    service = CupService()
    return await service.delete_entity(guid)
