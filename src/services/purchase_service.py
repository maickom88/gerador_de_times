from fastapi import HTTPException

from src.enums.roles_enum import RolesEnum
from src.models.purchase_model import PurchaseInput
from src.repositories.purchase_repository import PurchaseRepository
from src.services.user_service import UserService


class PurchaseService:
    def __init__(self):
        self.repository = PurchaseRepository()
        self.userService = UserService()

    async def create(self, input: PurchaseInput):
        if input.guid_user is not None:
            user = await self.userService.get_entity_by_guid(input.guid_user)
            if user is not None:
                input.guid_user = user.id
                entity = await self.repository.create(input)
                if entity is not None:
                    await self.userService.update_status_account(user.guid, RolesEnum.PREMIUM)
                    return entity
        raise HTTPException(status_code=400, detail="Guid User is required")

    async def update(self, input: PurchaseInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Purchase is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Purchase not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def get_entity(self, **kwargs):
        return await self.repository.get_entity(**kwargs)

    async def get_purchases_by_user(self, guid: str):
        user = await self.userService.get_entity_by_guid(guid)
        return await self.repository.get_purchases_by_user(id_user=user.id, deleted_at=None)

    async def get_active_purchase_by_player(self, guid: str):
        user = await self.userService.get_entity_by_guid(guid)
        return await self.repository.get_active_purchase_by_player(id_user=user.id, deleted_at=None)

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
