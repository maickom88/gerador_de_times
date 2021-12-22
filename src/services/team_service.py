from fastapi import HTTPException

from src.models.team_model import TeamUpdate, TeamInput
from src.repositories.team_repository import TeamRepository
from src.services.player_repository import PlayerService


class TeamService:
    def __init__(self):
        self.repository = TeamRepository()
        self.playerService = PlayerService()

    async def create(self, input: TeamInput):
        players = []
        for guid_player in input.guid_players:
            player = await self.playerService.get_entity_by_guid(guid_player)
            players.append(player)
        input.guid_players = players
        return await self.repository.create(input)

    async def update(self, input: TeamUpdate):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Team is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.color = input.color
        entity.name = input.name
        entity.goals = input.goals
        entity.goals_negative = input.goals_negative
        entity.victories = input.victories
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Team not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
