from src.settings.database import Base
from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class RelationTeamPlayer(Base):
    __tablename__ = "tb_relation_teams_players"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    player_id = Column(BigInteger, ForeignKey("tb_players.id"))
    team_id = Column(BigInteger, ForeignKey("tb_teams.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
