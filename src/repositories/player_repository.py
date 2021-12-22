import uuid
from datetime import datetime
from typing import List
from urllib.parse import unquote

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.player_model import PlayerInput
from src.schemas.player_schema import Player
from src.settings.logger import logger


class PlayerRepository:
    def __init__(self):
        self.db = db

    def query(self):
        return self.db.session.query(Player)

    async def get_entity_by_guid(self, guid: str) -> Player:
        try:
            return self.query().filter(Player.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Player:
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

    async def get_entities(self) -> List[Player]:
        try:
            return self.query().filter(Player.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_players_by_user(self, **kwargs) -> List[Player]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Player) -> Player:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: PlayerInput) -> Player:
        try:
            entity = Player()
            entity.guid = str(uuid.uuid4())
            entity.id_position = input.guid_position
            entity.id_skill = input.guid_skill
            entity.name = input.name
            entity.user_responsible = input.user_guid
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
