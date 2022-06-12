from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from src.settings.database import Base


class Goal(Base):
    __tablename__ = "tb_goals"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    id_player = Column(BigInteger, ForeignKey("tb_players.id"))
    player = relationship("Player", foreign_keys=[id_player], lazy="joined")
    time_goals = Column(String)
    id_match = Column(BigInteger, ForeignKey("tb_matches.id"))
    game = relationship("Match", foreign_keys=[id_match], lazy="joined")

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
