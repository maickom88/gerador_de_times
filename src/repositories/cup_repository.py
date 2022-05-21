import uuid
from datetime import datetime
from typing import List
from fastapi_sqlalchemy import db
from fastapi.responses import JSONResponse

from src.errors.business_error import BusinessError
from src.models.cup_model import CupInput
from src.repositories.relation_team_cup_repository import RelationCupTeamRepository
from src.schemas.cup_schema import Cup
from src.schemas.player_schema import Player
from src.schemas.team_schema import Team
from src.settings.logger import logger


class CupRepository:
    def __init__(self):
        self.db = db
        self.relationCupTeamRepository = RelationCupTeamRepository()

    def query(self, entity=Cup):
        return self.db.session.query(entity)

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

    async def get_cups_by_player(self, id_player: int) -> Cup:
        try:
            return self.query().filter(Team.players.any(id=id_player)).count()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_winner_cups_by_player(self, id_player: int) -> Cup:
        try:
            return self.query().join(Cup.winner, aliased=True) \
                .filter(Team.players.any(id=id_player)).count()
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_cup_winner(self, guid_cup: str) -> Team:
        try:
            entity = self.query().filter_by(guid=guid_cup).first()
            if len(entity.teams) > 0:
                team_winner = entity.teams[0]
                return team_winner
            return
        except Exception as e:
            raise BusinessError(
                f"Error on persist get a entity: {e}")

    async def get_best_goalkeeper_team_cup(self, guid_cup: str):
        try:
            entity = self.query().filter_by(guid=guid_cup).first()
            if len(entity.teams) > 0:
                team_with_the_lowest_negative_balance: Team = None
                goalkeeper: Player = None
                for team in entity.teams:
                    if team_with_the_lowest_negative_balance is None:
                        team_with_the_lowest_negative_balance = team
                    if team_with_the_lowest_negative_balance.goals_negative < team.goals_negative:
                        team_with_the_lowest_negative_balance = team
                for player in team_with_the_lowest_negative_balance.players:
                    if player.position.name.upper() == 'Goleiro'.upper():
                        goalkeeper = player
                if goalkeeper is None:
                    return JSONResponse(
                        status_code=404,
                        content={"detail": 'Goalkeeper not informed'}
                    )
                return goalkeeper
            return
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

    async def finishing_cup(self, entity: Cup) -> Cup:
        try:
            team = await self.get_cup_winner(entity.guid)
            entity.is_draft = False
            entity.id_team = team.id
            self.db.session.add(entity)
            self.db.session.flush()
            return await self.get_entity_by_guid(entity.guid)
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
