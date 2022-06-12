from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.settings.database import Base


class Team(Base):
    __tablename__ = "tb_teams"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    name = Column(String)
    color = Column(String)
    victories = Column(Integer)
    goals = Column(Integer)
    goals_negative = Column(Integer)
    players = relationship(
        "Player", secondary='tb_relation_teams_players', lazy="joined")

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
