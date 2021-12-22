import uuid
from datetime import datetime
from typing import List
from urllib.parse import unquote

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.position_model import PositionInput
from src.schemas.position_schema import Position
from src.settings.logger import logger


class PositionRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(Position)

    async def get_entity_by_guid(self, guid: str) -> Position:
        try:
            return self.query().filter(Position.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Position:
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

    async def get_entities(self) -> List[Position]:
        try:
            return self.query().filter(Position.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Position) -> Position:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: PositionInput) -> Position:
        try:
            entity = Position()
            entity.id_sport = input.sport_guid
            entity.name = input.name
            entity.description = input.description
            entity.guid = str(uuid.uuid4())
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
