from typing import List
from fastapi import APIRouter, Depends

from src.authenticator.auth import get_token
from src.models.purchase_model import PurchaseOutput, PurchaseInput
from src.services.purchase_service import PurchaseService
from src.settings.logger import logger

router = APIRouter()
purchase_router = {
    "router": router,
    "prefix": "/purchase",
    "tags": ["Purchase"],
    "dependencies": [Depends(get_token)]
}


@router.get(path="", response_model=List[PurchaseOutput])
async def get_purchases():
    logger.info("Starting request to get_purchases")
    service = PurchaseService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=PurchaseOutput)
async def get_purchase(guid: str):
    logger.info("Starting request to get_purchase")
    service = PurchaseService()
    return await service.get_entity_by_guid(guid)


@router.get(path="/user/{guid}", response_model=List[PurchaseOutput])
async def get_total_purchases_by_player(guid: str):
    logger.info("Starting request to get_total_purchases_by_user")
    service = PurchaseService()
    return await service.get_purchases_by_user(guid)


@router.get(path="/active/user/{guid}", response_model=PurchaseOutput)
async def get_active_purchase_by_player(guid: str):
    logger.info("Starting request to get_active_purchase_by_user")
    service = PurchaseService()
    return await service.get_active_purchase_by_player(guid)


@router.post(path="", response_model=PurchaseOutput, status_code=201)
async def register_purchase(purchase: PurchaseInput):
    logger.info("Starting request to register_purchase")
    service = PurchaseService()
    return await service.create(purchase)


@router.put(path="", response_model=PurchaseOutput, status_code=201)
async def update_purchase(purchase: PurchaseInput):
    logger.info("Starting request to update_purchase")
    service = PurchaseService()
    return await service.update(purchase)


@router.delete(path="/{guid}", status_code=204)
async def delete_purchase(guid: str):
    logger.info("Starting request to delete_purchase")
    service = PurchaseService()
    return await service.delete_entity(guid)
