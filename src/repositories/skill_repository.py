import uuid
from datetime import datetime
from typing import List
from urllib.parse import unquote

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.skiil_model import SkillInput
from src.schemas.skill_schema import Skill
from src.settings.logger import logger


class SkillRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(Skill)

    async def get_entity_by_guid(self, guid: str) -> Skill:
        try:
            return self.query().filter(Skill.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Skill:
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

    async def get_entities(self) -> List[Skill]:
        try:
            return self.query().filter(Skill.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Skill) -> Skill:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, entity: SkillInput) -> Skill:
        try:
            entity.guid = str(uuid.uuid4())
            entity = Skill(**entity.dict())
            try:
                entity.photo = unquote(input.photo)
            except Exception as e:
                print(e)
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
