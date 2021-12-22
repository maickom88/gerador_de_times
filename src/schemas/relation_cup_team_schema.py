from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from src.settings.database import Base


class RelationCupTeam(Base):
    __tablename__ = "tb_relation_cups_teams"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    team_id = Column(BigInteger, ForeignKey("tb_teams.id"))
    cup_id = Column(BigInteger, ForeignKey("tb_cups.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
