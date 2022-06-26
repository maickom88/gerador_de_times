import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.device_model import DeviceInput
from src.schemas.device_schema import Device
from src.settings.logger import logger


class DeviceRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(Device)

    async def get_entity_by_guid(self, guid: str) -> Device:
        try:
            return self.query().filter(Device.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Device:
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

    async def get_entities(self) -> List[Device]:
        try:
            return self.query().filter(Device.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_devices_by_user(self, **kwargs) -> List[Device]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Device) -> Device:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: DeviceInput) -> Device:
        try:
            entity = Device()
            entity.guid = str(uuid.uuid4())
            entity.token = input.token
            entity.platform = input.platform
            self.db.session.add(entity)
            self.db.session.flush()
            return entity

        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
