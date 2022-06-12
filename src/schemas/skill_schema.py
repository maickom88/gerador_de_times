from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, Integer
from sqlalchemy.dialects.postgresql import UUID

from src.settings.database import Base


class Skill(Base):
    __tablename__ = "tb_skills"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    strength = Column(Integer, default=0)
    velocity = Column(Integer, default=0)
    completion = Column(Integer, default=0)
    dribble = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
