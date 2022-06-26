import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.notification_model import NotificationInput
from src.schemas.notification_schema import Notification
from src.settings.logger import logger


class NotificationRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(Notification)

    async def get_entity_by_guid(self, guid: str) -> Notification:
        try:
            return self.query().filter(Notification.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Notification:
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

    async def get_entities(self) -> List[Notification]:
        try:
            return self.query().filter(Notification.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_notifications_by_user(self, **kwargs) -> List[Notification]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Notification) -> Notification:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: NotificationInput) -> Notification:
        try:
            entity = Notification()
            entity.guid = str(uuid.uuid4())
            entity.title = input.title
            entity.description = input.description
            entity.id_user = input.guid_user
            entity.is_read = False
            entity.data = input.data
            entity.navigate_to = input.navigate_to

            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
