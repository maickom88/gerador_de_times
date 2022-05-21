from typing import List
from fastapi import APIRouter, Depends

from src.authenticator.auth import get_token
from src.models.cup_model import CupOutput, CupInput
from src.models.player_cup_model import PlayerCupOutput, PlayerWinnerOutput
from src.models.player_model import PlayerOutput
from src.models.team_model import TeamOutput
from src.services.cup_service import CupService
from src.settings.logger import logger

router = APIRouter()
cup_router = {
    "router": router,
    "prefix": "/cup",
    "tags": ["Cup"],
    "dependencies": [Depends(get_token)]
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


@router.get(path="/player/{guid}", response_model=PlayerCupOutput)
async def get_total_cups_by_player(guid: str):
    logger.info("Starting request to get_total_cups_by_player")
    service = CupService()
    total_cups = await service.get_cups_by_player(guid)
    return {"total_number_of_cup_participations": total_cups}


@router.get(path="/winner/player/{guid}", response_model=PlayerWinnerOutput)
async def get_total_winner_by_player(guid: str):
    logger.info("Starting request to get_total_winner_by_player")
    service = CupService()
    total_winner_cups = await service.get_winner_cups_by_player(guid)
    return {"total_number_of_winner_cup": total_winner_cups}


@router.post(path="", response_model=CupOutput, status_code=201)
async def register_cup(cup: CupInput):
    logger.info("Starting request to register_cup")
    service = CupService()
    return await service.create(cup)


@router.post(path="/{guid}/finishing", response_model=CupOutput, status_code=201)
async def finishing_cup(guid: str):
    logger.info("Starting request to finishing_cup")
    service = CupService()
    return await service.finishing_cup(guid=guid)


@router.get(path="/{guid}/winner", response_model=TeamOutput, status_code=201)
async def get_cup_winner(guid: str):
    logger.info("Starting request to get_team_winner")
    service = CupService()
    return await service.get_cup_winner(guid_cup=guid)


@router.get(path="/{guid}/worst-team", response_model=TeamOutput, status_code=201)
async def get_worst_team_cup(guid: str):
    logger.info("Starting request to get_worst_team_cup")
    service = CupService()
    return await service.get_worst_team_cup(guid_cup=guid)


@router.get(path="/{guid}/best-goalkeeper", response_model=PlayerOutput, status_code=201)
async def get_best_goalkeeper_team_cup(guid: str):
    logger.info("Starting request to get_best_goalkeeper_team_cup")
    service = CupService()
    return await service.get_best_goalkeeper_team_cup(guid_cup=guid)


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
