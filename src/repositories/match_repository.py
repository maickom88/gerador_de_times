import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.match_model import MatchInput
from src.schemas.match_schema import Match
from src.settings.logger import logger


class MatchRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(Match)

    async def get_entity_by_guid(self, guid: str) -> Match:
        try:
            return self.query().filter(Match.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Match:
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

    async def get_entities(self) -> List[Match]:
        try:
            return self.query().filter(Match.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_matches_by_cup(self, **kwargs) -> List[Match]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_matches_by_team(self, **kwargs) -> List[Match]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Match) -> Match:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: MatchInput) -> Match:
        try:
            entity = Match()
            entity.guid = str(uuid.uuid4())
            entity.id_cup = input.guid_cup
            entity.id_opposing_team = input.guid_opposing_team
            entity.id_home_team = input.guid_home_team
            entity.time = input.time
            entity.time_additions = input.time_additions
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
