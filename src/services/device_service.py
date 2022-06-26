from fastapi import HTTPException

from src.models.device_model import DeviceInput
from src.repositories.device_repository import DeviceRepository
from src.services.user_service import UserService


class DeviceService:
    def __init__(self):
        self.repository = DeviceRepository()
        self.userService = UserService()

    async def create(self, input: DeviceInput):
        if input.guid is None:
            entity = await self.get_devices_by_user(input.guid_user)
            if len(entity) > 0:
                return await self.update(input)
            if input.guid_user is not None:
                user = await self.userService.get_entity_by_guid(input.guid_user)
                input.guid_user = user.id
                return await self.repository.create(input)
        return await self.update(input)

    async def update(self, input: DeviceInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Device is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.token = input.token
        entity.platform = input.platform
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Device not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def get_tokens(self):
        entities = await self.repository.get_entities()
        return map(lambda entity: entity.token, entities)

    async def get_entity(self, **kwargs):
        return await self.repository.get_entity(**kwargs)

    async def get_devices_by_user(self, guid: str):
        user = await self.userService.get_entity_by_guid(guid)
        return await self.repository.get_devices_by_user(id_user=user.id, deleted_at=None)

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
