from fastapi import HTTPException


from src.models.position_model import PositionInput
from src.repositories.position_repository import PositionRepository
from src.services.sport_service import SportService


class PositionService:
    def __init__(self):
        self.repository = PositionRepository()
        self.sportService = SportService()

    async def create(self, input: PositionInput):
        sport = await self.sportService.get_entity_by_guid(input.sport_guid)
        input.sport_guid = sport.id
        return await self.repository.create(input)

    async def update(self, input: PositionInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Position is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.name = input.name
        entity.description = input.description
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Position not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
