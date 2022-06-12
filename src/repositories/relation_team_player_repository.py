import uuid
from datetime import datetime
from typing import List
from urllib.parse import unquote

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.schemas.relation_team_player_schema import RelationTeamPlayer
from src.settings.logger import logger


class RelationTeamPlayerRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(RelationTeamPlayer)

    async def get_entity_by_guid(self, guid: str) -> RelationTeamPlayer:
        try:
            return self.query().filter(RelationTeamPlayer.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> RelationTeamPlayer:
        try:
            return self.query().filter_by(**kwargs).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def delete_entity(self, guid: str):
        entity = await self.get_entity_by_guid(guid)
        if entity is not None:
            entity.deleted_at = datetime.utcnow()
            await self.update(entity)
        else:
            raise BusinessError("Entity doesn't exists")

    async def get_entities(self) -> List[RelationTeamPlayer]:
        try:
            return self.query().filter(RelationTeamPlayer.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: RelationTeamPlayer) -> RelationTeamPlayer:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, id_team: str, id_player: str) -> RelationTeamPlayer:
        try:
            entity = RelationTeamPlayer()
            entity.player_id = id_player
            entity.team_id = id_team
            entity.guid = str(uuid.uuid4())
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
