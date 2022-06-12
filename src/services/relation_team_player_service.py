from fastapi import HTTPException

from src.repositories.relation_team_player_repository import RelationTeamPlayerRepository


class RelationTeamPlayerService:
    def __init__(self):
        self.repository = RelationTeamPlayerRepository()

    async def create(self, id_team: str, id_player):
        return await self.repository.create(id_team, id_player)

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
