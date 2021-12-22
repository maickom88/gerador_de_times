from typing import List
from fastapi import APIRouter

from src.models.team_model import TeamOutput, TeamInput, TeamUpdate
from src.services.team_service import TeamService
from src.settings.logger import logger

router = APIRouter()
team_router = {
    "router": router,
    "prefix": "/team",
    "tags": ["Team"],
}


@router.get(path="", response_model=List[TeamOutput])
async def get_teams():
    logger.info("Starting request to get_teams")
    service = TeamService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=TeamOutput)
async def get_team(guid: str):
    logger.info("Starting request to get_team")
    service = TeamService()
    return await service.get_entity_by_guid(guid)


@router.post(path="", response_model=TeamOutput, status_code=201)
async def register_team(team: TeamInput):
    logger.info("Starting request to register_team")
    service = TeamService()
    return await service.create(team)


@router.put(path="", response_model=TeamOutput, status_code=201)
async def update_team(team: TeamUpdate):
    logger.info("Starting request to update_team")
    service = TeamService()
    return await service.update(team)


@router.delete(path="/{guid}", status_code=204)
async def delete_team(guid: str):
    logger.info("Starting request to delete_team")
    service = TeamService()
    return await service.delete_entity(guid)
