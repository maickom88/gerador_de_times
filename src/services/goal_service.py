from fastapi import HTTPException

from src.models.goal_model import GoalInput
from src.repositories.goal_repository import GoalRepository
from src.services.cup_service import CupService
from src.services.match_service import MatchService
from src.services.player_repository import PlayerService


class GoalService:
    def __init__(self):
        self.repository = GoalRepository()
        self.playerService = PlayerService()
        self.cupService = CupService()
        self.matchService = MatchService()

    async def create(self, input: GoalInput):
        player = await self.playerService.get_entity_by_guid(input.guid_player)
        input.guid_player = player.id
        match = await self.matchService.get_entity_by_guid(input.guid_macth)
        input.guid_macth = match.id
        return await self.repository.create(input)

    async def update(self, input: GoalInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Goal is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Goal not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def get_goals_by_player(self, guid: str):
        player = await self.playerService.get_entity_by_guid(guid)
        return await self.repository.get_goals_by_player(id_player=player.id,  deleted_at=None)

    async def get_top_goals_player(self, guid: str):
        cup_id = None
        if guid is not None:
            cup = await self.cupService.get_entity_by_guid(guid)
            cup_id = cup.id
        return await self.repository.get_top_goals_player(cup_id=cup_id)

    async def get_goals_by_match(self, guid: str):
        match = await self.matchService.get_entity_by_guid(guid)
        return await self.repository.get_goals_by_match(id_match=match.id, deleted_at=None)

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
