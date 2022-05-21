import itertools

from fastapi import HTTPException

from src.models.match_model import MatchInput, MatchUpdate
from src.repositories.match_repository import MatchRepository
from src.services.cup_service import CupService
from src.services.team_service import TeamService


class MatchService:
    def __init__(self):
        self.repository = MatchRepository()
        self.cupService = CupService()
        self.teamService = TeamService()

    async def create(self, input: MatchInput):
        cup = await self.cupService.get_entity_by_guid(input.guid_cup)
        input.guid_cup = cup.id
        team_home = await self.teamService.get_entity_by_guid(input.guid_home_team)
        input.guid_home_team = team_home.id
        opposing_team = await self.teamService.get_entity_by_guid(input.guid_opposing_team)
        input.guid_opposing_team = opposing_team.id
        return await self.repository.create(input)

    async def update(self, input: MatchUpdate):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Match is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.final_time = input.final_time
        entity.total_time_pause = input.total_time_pause
        entity.total_goals = input.total_goals

        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Match not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def get_matches_by_cup(self, guid: str):
        cup = await self.cupService.get_entity_by_guid(guid)
        return await self.repository.get_matches_by_cup(id_cup=cup.id, deleted_at=None)

    async def get_matches_by_team(self, guid: str):
        team = await self.teamService.get_entity_by_guid(guid)
        matches_home = await self.repository \
            .get_matches_by_team(id_home_team=team.id, deleted_at=None)
        matches_opposing = await self.repository \
            .get_matches_by_team(id_opposing_team=team.id, deleted_at=None)
        return list(itertools.chain(matches_home, matches_opposing))

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
