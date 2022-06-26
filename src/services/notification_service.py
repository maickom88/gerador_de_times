from fastapi import HTTPException

from src.models.notification_model import NotificationInput
from src.repositories.notification_repository import NotificationRepository
from src.services.user_service import UserService


class NotificationService:
    def __init__(self):
        self.repository = NotificationRepository()
        self.userService = UserService()

    async def create(self, input: NotificationInput):
        if input.guid_user is not None:
            user = await self.userService.get_entity_by_guid(input.guid_user)
            input.guid_user = user.id
            return await self.repository.create(input)
        users = await self.userService.get_entities()
        for user in users:
            input.guid_user = user.id
            await self.repository.create(input)
        return input

    async def update(self, input: NotificationInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Notification is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        return await self.repository.update(entity)

    async def clear(self, guid_user: str):
        if guid_user is None or len(guid_user) < 32:
            raise HTTPException(status_code=400, detail="Guid Notification is required")
        entities = await self.get_notifications_by_user(guid_user)
        if len(entities) > 0:
            for entity in entities:
                await self.repository.delete_entity(entity.guid)
        return

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Notification not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def get_entity(self, **kwargs):
        return await self.repository.get_entity(**kwargs)

    async def get_notifications_by_user(self, guid: str):
        user = await self.userService.get_entity_by_guid(guid)
        return await self.repository.get_notifications_by_user(id_user=user.id, deleted_at=None)

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
