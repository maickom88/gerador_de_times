from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.settings.database import Base


class Players(Base):
    __tablename__ = "tb_players"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    name = Column(String)
    id_position = Column(BigInteger, ForeignKey("tb_positions.id"))
    position = relationship("Positions", foreign_keys=[id_position], lazy="joined")
    photo = Column(String)
    id_skill = Column(BigInteger, ForeignKey("tb_skills.id"))
    skills = relationship("Skills", foreign_keys=[id_skill], lazy="joined")
    user_responsible = Column(BigInteger, ForeignKey("tb_users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
