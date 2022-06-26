from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, Float, Enum
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.enums.plataform_enum import PlatformEnum
from src.settings.database import Base


class Purchase(Base):
    __tablename__ = "tb_purchases"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    id_user = Column(BigInteger, ForeignKey("tb_users.id"))
    user = relationship("User", foreign_keys=[id_user], lazy="joined")
    date_purchase = Column(DateTime, default=datetime.utcnow)
    date_expired_purchase = Column(DateTime, default=datetime.utcnow)
    price_usd = Column(Float)
    price_br = Column(Float)
    platform = Column(Enum(PlatformEnum), default=PlatformEnum.ANDROID)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
