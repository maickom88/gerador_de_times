from typing import List, Optional
from fastapi import APIRouter, Depends, responses
from starlette.status import HTTP_204_NO_CONTENT

from src.authenticator.auth import get_token
from src.models.goal_model import GoalOutput, GoalInput
from src.models.goal_player_model import GoalPlayerOutput
from src.services.goal_service import GoalService
from src.settings.logger import logger

router = APIRouter()
goal_router = {
    "router": router,
    "prefix": "/goal",
    "tags": ["Goal"],
    "dependencies": [Depends(get_token)]
}


@router.get(path="", response_model=List[GoalOutput])
async def get_goal():
    logger.info("Starting request to get_goal")
    service = GoalService()
    return await service.get_entities()


@router.get(path="/top-player", response_model=GoalPlayerOutput)
async def get_top_goals_player(guid_cup: Optional[str] = None):
    logger.info("Starting request to get_top_goals_player")
    service = GoalService()
    return await service.get_top_goals_player(guid_cup)


@router.get(path="/{guid}", response_model=GoalOutput)
async def get_goal(guid: str):
    logger.info("Starting request to get_goal")
    service = GoalService()
    return await service.get_entity_by_guid(guid)


@router.post(path="", response_model=GoalOutput, status_code=201)
async def register_goal(goal: GoalInput):
    logger.info("Starting request to register_goal")
    service = GoalService()
    return await service.create(goal)


@router.put(path="", response_model=GoalOutput, status_code=201)
async def update_goal(goal: GoalInput):
    logger.info("Starting request to update_goal")
    service = GoalService()
    return await service.update(goal)


@router.get(path="/player/{guid}", response_model=List[GoalOutput])
async def get_goals_by_player(guid: str):
    logger.info("Starting request to get_goals_by_player")
    service = GoalService()
    return await service.get_goals_by_player(guid)


@router.get(path="/match/{guid}", response_model=List[GoalOutput])
async def get_goals_by_match(guid: str):
    logger.info("Starting request to get_goals_by_match")
    service = GoalService()
    return await service.get_goals_by_match(guid)


@router.delete(path="/{guid}", status_code=204)
async def delete_goal(guid: str):
    logger.info("Starting request to delete_goal")
    service = GoalService()
    await service.delete_entity(guid)
    return responses.Response(status_code=HTTP_204_NO_CONTENT)
