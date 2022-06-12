import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db

from src.errors.business_error import BusinessError
from src.models.team_model import TeamInput
from src.repositories.relation_team_player_repository import RelationTeamPlayerRepository
from src.schemas.team_schema import Team
from src.settings.logger import logger


class TeamRepository:
    def __init__(self):
        self.db = db
        self.relationTeamPlayerRepository = RelationTeamPlayerRepository()

    def query(self):
        return self.db.session.query(Team)

    async def get_entity_by_guid(self, guid: str) -> Team:
        try:
            return self.query().filter(Team.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Team:
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

    async def get_entities(self) -> List[Team]:
        try:
            return self.query().filter(Team.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Team) -> Team:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: TeamInput) -> Team:
        try:
            entity = Team()
            entity.guid = str(uuid.uuid4())
            entity.name = input.name
            entity.players = input.guid_players
            entity.victories = input.victories
            entity.goals_negative = input.goals_negative
            entity.goals = input.goals
            entity.color = input.color
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
