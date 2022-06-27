from typing import List
from fastapi import APIRouter, Depends

from src.authenticator.auth import get_token
from src.models.notification_model import NotificationOutput, NotificationInput
from src.services.notification_service import NotificationService
from src.settings.logger import logger

router = APIRouter()
notification_router = {
    "router": router,
    "prefix": "/notification",
    "tags": ["Notification"],
    "dependencies": [Depends(get_token)]
}


@router.get(path="", response_model=List[NotificationOutput])
async def get_notifications():
    logger.info("Starting request to get_notifications")
    service = NotificationService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=NotificationOutput)
async def get_notification(guid: str):
    logger.info("Starting request to get_notification")
    service = NotificationService()
    return await service.get_entity_by_guid(guid)


@router.get(path="/user/{guid}", response_model=List[NotificationOutput])
async def get_total_notifications_by_player(guid: str):
    logger.info("Starting request to get_total_notifications_by_user")
    service = NotificationService()
    return await service.get_notifications_by_user(guid)


@router.post(path="", response_model=NotificationOutput, status_code=201)
async def register_notification(notification: NotificationInput):
    logger.info("Starting request to register_notification")
    service = NotificationService()
    return await service.create(notification)


@router.put(path="", response_model=NotificationOutput, status_code=201)
async def update_notification(notification: NotificationInput):
    logger.info("Starting request to update_notification")
    service = NotificationService()
    return await service.update(notification)


@router.put(path="/clear/user/{guid}", status_code=201)
async def update_notification(guid: str):
    logger.info("Starting request to update_notification")
    service = NotificationService()
    return await service.clear(guid)


@router.delete(path="/{guid}", status_code=204)
async def delete_notification(guid: str):
    logger.info("Starting request to delete_notification")
    service = NotificationService()
    return await service.delete_entity(guid)
