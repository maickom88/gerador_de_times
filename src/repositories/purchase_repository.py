import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db
from sqlalchemy import desc

from src.errors.business_error import BusinessError
from src.models.purchase_model import PurchaseInput
from src.schemas.purchase_schema import Purchase
from src.settings.logger import logger


class PurchaseRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(Purchase)

    async def get_entity_by_guid(self, guid: str) -> Purchase:
        try:
            return self.query().filter(Purchase.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Purchase:
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

    async def get_entities(self) -> List[Purchase]:
        try:
            return self.query().filter(Purchase.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_purchases_by_user(self, **kwargs) -> List[Purchase]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_active_purchase_by_player(self, **kwargs) -> Purchase:
        try:
            return self.query().filter_by(**kwargs).order_by(desc(Purchase.id)).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Purchase) -> Purchase:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: PurchaseInput) -> Purchase:
        try:
            entity = Purchase()
            entity.guid = str(uuid.uuid4())
            entity.id_user = input.guid_user
            entity.date_purchase = datetime.utcnow()
            entity.date_expired_purchase = entity.date_purchase + datetime.timedelta(days=30)
            entity.platform = input.platform
            entity.price_br = input.price_br
            entity.price_usd = input.price_usd

            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
