import uuid
from datetime import datetime
from typing import List

from fastapi_sqlalchemy import db
from sqlalchemy import func, desc

from src.errors.business_error import BusinessError
from src.models.goal_model import GoalInput
from src.schemas.cup_schema import Cup
from src.schemas.goal_schema import Goal
from src.schemas.match_schema import Match
from src.services.player_repository import PlayerService
from src.settings.logger import logger


class GoalRepository:
    def __init__(self):
        self.db = db
        self.playerService = PlayerService()

    def query(self, entity=Goal, args=None):
        if args is None:
            return self.db.session.query(entity)
        return self.db.session.query(entity, args)

    async def get_entity_by_guid(self, guid: str) -> Goal:
        try:
            return self.query().filter(Goal.guid == guid).first()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_entity(self, **kwargs) -> Goal:
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

    async def get_entities(self) -> List[Goal]:
        try:
            return self.query().filter(Goal.deleted_at.is_(None)).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_goals_by_player(self, **kwargs) -> List[Goal]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_top_goals_player(self, cup_id: str):
        try:
            goals = None
            player = None
            if cup_id is not None:
                entity = self.query(Goal.id_player, func.count(Goal.id).
                                    label('goals')).join(Goal.game).filter(Match.id_cup == cup_id) \
                    .group_by(Goal.id_player).order_by(desc('goals')).first()
            else:
                entity = self.query(Goal.id_player, func.count(Goal.id).
                                    label('goals')).join(Goal.game)\
                    .group_by(Goal.id_player).order_by(desc('goals')).first()
            if entity is not None:
                player = await self.playerService.get_entity(id=entity.id_player)
                goals = entity.goals
            return {"goals": goals, "player": player}
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_goals_by_match(self, **kwargs) -> List[Goal]:
        try:
            return self.query().filter_by(**kwargs).all()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def update(self, entity: Goal) -> Goal:
        try:
            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")

    async def create(self, input: GoalInput) -> Goal:
        try:
            entity = Goal()
            entity.guid = str(uuid.uuid4())
            entity.id_player = input.guid_player
            entity.id_match = input.guid_macth
            entity.time_goals = input.time_goals

            self.db.session.add(entity)
            self.db.session.flush()
            return entity
        except Exception as e:
            self.db.session.rollback()
            logger.error(f"Error on persist entity: {entity.dict()}: {e}")
            raise BusinessError(
                f"Error on persist entity: {entity.dict()}: {e}")
