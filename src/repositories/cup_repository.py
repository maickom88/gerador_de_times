import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.cup_model import CupInput
from src.repositories.relation_team_cup_repository import RelationCupTeamRepository
from src.schemas.cup_schema import Cup
from src.settings.logger import logger


class CupRepository:
    def __init__(self):
        self.db = db
        self.relationCupTeamRepository = RelationCupTeamRepository()

    def query(self):
        return self.db.session.query(Cup)

    async def get_entity_by_guid(self, guid: str) -> Cup:
        try:
            return self.query().filter(Cup.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Cup:
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

    async def get_entities(self) -> List[Cup]:
        try:
            return self.query().filter(Cup.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Cup) -> Cup:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: CupInput) -> Cup:
        try:
            entity = Cup()
            entity.guid = str(uuid.uuid4())
            entity.teams = input.guid_teams
            entity.time_additions = input.time_additions
            entity.time = input.time
            entity.id_sport = input.guid_sport
            entity.is_draft = input.is_draft
            entity.responsible_email = input.responsible_email
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
