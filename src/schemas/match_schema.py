from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, Integer
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.settings.database import Base


class Match(Base):
    __tablename__ = "tb_matches"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    id_opposing_team = Column(BigInteger, ForeignKey("tb_teams.id"))
    opposing_team = relationship("Team", foreign_keys=[id_opposing_team], lazy="joined")
    id_home_team = Column(BigInteger, ForeignKey("tb_teams.id"))
    home_team = relationship("Team", foreign_keys=[id_home_team], lazy="joined")
    id_cup = Column(BigInteger, ForeignKey("tb_cups.id"))
    cup = relationship("Cup", foreign_keys=[id_cup], lazy="joined")
    total_goals = Column(Integer)
    time = Column(Integer)
    time_additions = Column(Integer)
    total_time_pause = Column(Integer)
    final_time = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
