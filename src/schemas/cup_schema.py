from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy import Column, String, \
    DateTime, BigInteger, Integer, Boolean
from sqlalchemy.orm import relationship

from src.settings.database import Base


class Cup(Base):
    __tablename__ = "tb_cups"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    id_team = Column(BigInteger, ForeignKey("tb_teams.id"))
    winner = relationship("Team", foreign_keys=[id_team], lazy="joined")
    responsible_email = Column(String)
    id_sport = Column(BigInteger, ForeignKey("tb_sports.id"))
    sport = relationship("Sport", foreign_keys=[id_sport], lazy="joined")
    time = Column(Integer)
    time_additions = Column(Integer)
    is_draft = Column(Boolean, default=True)
    teams = relationship("Team", secondary="tb_relation_cups_teams", lazy="joined")

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
