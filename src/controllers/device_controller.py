from typing import List
from fastapi import APIRouter, Depends

from src.authenticator.auth import get_token
from src.models.device_model import DeviceOutput, DeviceInput
from src.services.device_service import DeviceService
from src.settings.logger import logger

router = APIRouter()
device_router = {
    "router": router,
    "prefix": "/device",
    "tags": ["Device"],
    "dependencies": [Depends(get_token)]
}


@router.get(path="", response_model=List[DeviceOutput])
async def get_devices():
    logger.info("Starting request to get_devices")
    service = DeviceService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=DeviceOutput)
async def get_device(guid: str):
    logger.info("Starting request to get_device")
    service = DeviceService()
    return await service.get_entity_by_guid(guid)


@router.get(path="/user/{guid}", response_model=List[DeviceOutput])
async def get_total_devices_by_player(guid: str):
    logger.info("Starting request to get_total_devices_by_user")
    service = DeviceService()
    return await service.get_devices_by_user(guid)


@router.post(path="", response_model=DeviceOutput, status_code=201)
async def register_device(device: DeviceInput):
    logger.info("Starting request to register_device")
    service = DeviceService()
    return await service.create(device)


@router.put(path="", response_model=DeviceOutput, status_code=201)
async def update_device(device: DeviceInput):
    logger.info("Starting request to update_device")
    service = DeviceService()
    return await service.update(device)


@router.delete(path="/{guid}", status_code=204)
async def delete_device(guid: str):
    logger.info("Starting request to delete_device")
    service = DeviceService()
    return await service.delete_entity(guid)
