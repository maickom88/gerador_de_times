from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, String, Enum
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.enums.plataform_enum import PlatformEnum
from src.settings.database import Base


class Device(Base):
    __tablename__ = "tb_devices"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    id_user = Column(BigInteger, ForeignKey("tb_users.id"))
    user = relationship("User", foreign_keys=[id_user], lazy="joined")
    token = Column(String)
    platform = Column(Enum(PlatformEnum), default=PlatformEnum.ANDROID)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
