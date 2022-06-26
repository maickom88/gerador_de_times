from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from src.enums.plataform_enum import PlatformEnum
from src.models.user_model import UserOutput


class PurchaseInput(BaseModel):
    guid: Optional[str] = Field(None)
    guid_user: Optional[str] = Field(None)
    price_br: Optional[float] = Field(None)
    price_usd: Optional[float] = Field(None)
    platform: PlatformEnum = Field(None)

    class Config:
        orm_mode = True


class PurchaseOutput(BaseModel):
    guid: Optional[str] = Field(None)
    user: UserOutput = Field(None)
    date_purchase: datetime = Field(None)
    date_expired_purchase: datetime = Field(None)
    price_br: Optional[float] = Field(None)
    price_usd: Optional[float] = Field(None)
    platform: PlatformEnum = Field(None)

    class Config:
        orm_mode = True
