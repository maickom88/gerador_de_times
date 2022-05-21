from typing import List, Optional

from fastapi import APIRouter, Depends

from fastapi.routing import Request
from src.authenticator.auth import get_token
from src.models.user_model import UserInput, UserOutput
from src.services.user_service import UserService
from src.settings.logger import logger

router = APIRouter()
user_router = {
    "router": router,
    "prefix": "/user",
    "tags": ["User"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="", status_code=201, response_model=UserOutput)
async def register_user(input: UserInput):
    logger.info("Starting request to user_controller.register_user")

    service = UserService()
    return await service.create(input)


@router.get(path="", response_model=List[UserOutput])
async def get_users():
    logger.info("Starting request to user_controller.get_users")

    service = UserService()
    return await service.get_entities()


@router.put(path="/notifier", response_model=UserOutput)
async def notifier(request: Request,  name: Optional[str] = None):
    logger.info("Starting request to user_controller.notifier")
    token = request.headers["x-api-key"]
    service = UserService()
    return await service.notifier(token, name)


@router.get(path="/{guid}", response_model=UserOutput)
async def get_user(guid: str):
    logger.info("Starting request to user_controller.get_user")

    service = UserService()
    return await service.get_entity_by_guid(guid)


@router.put(path="", response_model=UserOutput)
async def update_user(input: UserInput):
    logger.info("Starting request to user_controller.update_user")

    service = UserService()
    return await service.update(input)


@router.delete(path="/{guid}", status_code=204)
async def delete_user(guid: str):
    logger.info("Starting request to user_controller.delete_user")

    service = UserService()
    return await service.delete_entity(guid)
