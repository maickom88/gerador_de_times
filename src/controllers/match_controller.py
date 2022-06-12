from typing import List
from fastapi import APIRouter

from src.models.match_model import MatchOutput, MatchUpdate, MatchInput
from src.services.match_service import MatchService
from src.settings.logger import logger

router = APIRouter()
match_router = {
    "router": router,
    "prefix": "/match",
    "tags": ["Match"],
}


@router.get(path="", response_model=List[MatchOutput])
async def get_matches():
    logger.info("Starting request to get_matches")
    service = MatchService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=MatchOutput)
async def get_match(guid: str):
    logger.info("Starting request to get_match")
    service = MatchService()
    return await service.get_entity_by_guid(guid)


@router.get(path="/cup/{guid}", response_model=List[MatchOutput])
async def get_matches_by_cup(guid: str):
    logger.info("Starting request to get_matches_by_cup")
    service = MatchService()
    return await service.get_matches_by_cup(guid)


@router.get(path="/team/{guid}", response_model=List[MatchOutput])
async def get_matches_by_team(guid: str):
    logger.info("Starting request to get_matches_by_cup")
    service = MatchService()
    return await service.get_matches_by_team(guid)


@router.post(path="", response_model=MatchOutput, status_code=201)
async def register_match(match: MatchInput):
    logger.info("Starting request to register_match")
    service = MatchService()
    return await service.create(match)


@router.put(path="", response_model=MatchOutput, status_code=201)
async def update_match(match: MatchUpdate):
    logger.info("Starting request to update_match")
    service = MatchService()
    return await service.update(match)


@router.delete(path="/{guid}", status_code=204)
async def delete_match(guid: str):
    logger.info("Starting request to delete_match")
    service = MatchService()
    return await service.delete_entity(guid)
