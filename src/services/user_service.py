from fastapi import HTTPException

from urllib.parse import unquote
from src.models.user_model import UserInput
from src.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def create(self, input: UserInput):
        user_exist = await self.verify_if_user_exist(email=input.email)
        if user_exist:
            entity = await self.repository.get_entity(email=input.email)
            entity.first_access = input.first_access
            return await self.repository.update(entity)
        return await self.repository.create(input)

    async def verify_if_user_exist(self, email: str) -> bool:
        entity = await self.repository.get_entity(email=email)
        if entity is not None:
            return True
        return False

    async def update_photo(self, photo: str, guid_user: str):
        user = await self.repository.get_entity_by_guid(guid_user)
        user.photo = photo
        await self.repository.update(user)

    async def update(self, input: UserInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid User is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.name = input.name
        entity.photo = unquote(input.photo)
        entity.first_access = input.first_access
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="User not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
