from typing import Optional
from pydantic import BaseModel, Field


class PositionInput(BaseModel):
    guid: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    sport_guid: Optional[str] = Field(None)

    class Config:
        orm_mode = True


class PositionOutput(BaseModel):
    guid: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)

    class Config:
        orm_mode = True
