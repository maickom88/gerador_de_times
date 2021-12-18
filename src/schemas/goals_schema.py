from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID

from src.settings.database import Base


class Goals(Base):
    __tablename__ = "tb_goals"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    player = Column(String)
    time_goals = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
