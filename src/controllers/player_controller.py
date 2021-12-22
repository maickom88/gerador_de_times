from typing import List
from fastapi import APIRouter

from src.models.player_model import PlayerOutput, PlayerInput
from src.services.player_repository import PlayerService
from src.settings.logger import logger

router = APIRouter()
player_router = {
    "router": router,
    "prefix": "/player",
    "tags": ["Player"],
}


@router.get(path="", response_model=List[PlayerOutput])
async def get_players():
    logger.info("Starting request to get_players")
    service = PlayerService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=PlayerOutput)
async def get_player(guid: str):
    logger.info("Starting request to get_player")
    service = PlayerService()
    return await service.get_entity_by_guid(guid)


@router.get(path="/user/{guid}", response_model=List[PlayerOutput])
async def get_players_by_user(guid: str):
    logger.info("Starting request to get_players_by_user")
    service = PlayerService()
    return await service.get_players_by_user(guid)


@router.post(path="", response_model=PlayerOutput, status_code=201)
async def register_player(sport: PlayerInput):
    logger.info("Starting request to register_player")
    service = PlayerService()
    return await service.create(sport)


@router.put(path="", response_model=PlayerOutput, status_code=201)
async def update_sport(sport: PlayerInput):
    logger.info("Starting request to update_sport")
    service = PlayerService()
    return await service.update(sport)


@router.delete(path="/{guid}", status_code=204)
async def delete_player(guid: str):
    logger.info("Starting request to delete_player")
    service = PlayerService()
    return await service.delete_entity(guid)
