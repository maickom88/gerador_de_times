from fastapi import HTTPException

from urllib.parse import unquote

from src.models.player_model import PlayerInput
from src.repositories.player_repository import PlayerRepository
from src.services.position_service import PositionService
from src.services.skill_service import SkillService
from src.services.user_service import UserService


class PlayerService:
    def __init__(self):
        self.repository = PlayerRepository()
        self.userService = UserService()
        self.positionService = PositionService()
        self.skillService = SkillService()

    async def create(self, input: PlayerInput):
        user = await self.userService.get_entity_by_guid(input.user_guid)
        input.user_guid = user.id
        position = await self.positionService.get_entity_by_guid(input.guid_position)
        input.guid_position = position.id
        skill = await self.skillService.get_entity_by_guid(input.guid_skill)
        input.guid_skill = skill.id
        return await self.repository.create(input)

    async def update(self, input: PlayerInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Player is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.name = input.name
        entity.photo = unquote(input.photo)
        if input.guid_position is not None:
            position = await self.positionService.get_entity_by_guid(input.guid_position)
            entity.id_position = position.id
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Player not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def get_players_by_user(self, guid: str):
        user = await self.userService.get_entity_by_guid(guid)
        return await self.repository.get_players_by_user(user_responsible=user.id, deleted_at=None)

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
