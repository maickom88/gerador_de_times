import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.schemas.relation_cup_team_schema import RelationCupTeam
from src.settings.logger import logger


class RelationCupTeamRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(RelationCupTeam)

    async def get_entity_by_guid(self, guid: str) -> RelationCupTeam:
        try:
            return self.query().filter(RelationCupTeam.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> RelationCupTeam:
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

    async def get_entities(self) -> List[RelationCupTeam]:
        try:
            return self.query().filter(RelationCupTeam.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: RelationCupTeam) -> RelationCupTeam:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, id_team: str, id_cup: str) -> RelationCupTeam:
        try:
            entity = RelationCupTeam()
            entity.team_id = id_team
            entity.cup_id = id_cup
            entity.guid = str(uuid.uuid4())
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
