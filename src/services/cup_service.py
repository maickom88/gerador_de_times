from fastapi import HTTPException

from src.models.cup_model import CupInput
from src.repositories.cup_repository import CupRepository
from src.services.player_repository import PlayerService
from src.services.sport_service import SportService
from src.services.team_service import TeamService


class CupService:
    def __init__(self):
        self.repository = CupRepository()
        self.teamService = TeamService()
        self.sportService = SportService()
        self.playerService = PlayerService()

    async def create(self, input: CupInput):
        teams = []
        sport = await self.sportService.get_entity_by_guid(input.guid_sport)
        input.guid_sport = sport.id
        for guid_team in input.guid_teams:
            team = await self.teamService.get_entity_by_guid(guid_team)
            teams.append(team)
        input.guid_teams = teams
        return await self.repository.create(input)

    async def update(self, input: CupInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid Cup is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.time = input.time
        entity.time_additions = input.time_additions
        entity.is_draft = input.is_draft
        if len(input.guid_teams) > 0:
            teams = []
            for guid_team in input.guid_teams:
                team = await self.teamService.get_entity_by_guid(guid_team)
                teams.append(team)
            entity.teams = teams
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="Cup not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def get_cups_by_player(self, guid_player):
        player = await self.playerService.get_entity_by_guid(guid_player)
        return await self.repository.get_cups_by_player(id_player=player.id)

    async def get_winner_cups_by_player(self, guid_player):
        player = await self.playerService.get_entity_by_guid(guid_player)
        return await self.repository.get_winner_cups_by_player(id_player=player.id)

    async def get_cup_winner(self, guid_cup: str):
        return await self.repository.get_cup_winner(guid_cup=guid_cup)

    async def get_worst_team_cup(self, guid_cup: str):
        return await self.repository.get_worst_team_cup(guid_cup=guid_cup)

    async def get_best_goalkeeper_team_cup(self, guid_cup: str):
        return await self.repository.get_best_goalkeeper_team_cup(guid_cup=guid_cup)

    async def finishing_cup(self, guid: str):
        cup = await self.repository.get_entity_by_guid(guid)
        return await self.repository.finishing_cup(entity=cup)

    async def delete_entity(self, guid: str):
        return await self.repository.delete_entity(guid)
