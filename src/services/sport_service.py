from fastapi import HTTPException

from urllib.parse import unquote

from src.models.sport_model import SportInput
from src.repositories.sport_repository import SportRepository


class SportService:
    def __init__(self):
        self.repository = SportRepository()

    async def create(self, input: SportInput):
        return await self.repository.create(input)

    async def update(self, input: SportInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Sport is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.name = input.name
        entity.photo = unquote(input.photo)
        entity.icon = input.icon
        entity.description = input.description
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Sport not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
