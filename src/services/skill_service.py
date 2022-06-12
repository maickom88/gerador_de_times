from fastapi import HTTPException

from src.models.skiil_model import SkillInput
from src.repositories.skill_repository import SkillRepository


class SkillService:
    def __init__(self):
        self.repository = SkillRepository()

    async def create(self, input: SkillInput):
        return await self.repository.create(input)

    async def update(self, input: SkillInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Skill is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.strength = input.strength
        entity.dribble = input.dribble
        entity.velocity = input.velocity
        entity.completion = input.completion
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Skill not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
