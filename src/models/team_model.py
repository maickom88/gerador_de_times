from typing import List, Optional
from pydantic import BaseModel, Field

from src.models.player_model import PlayerOutput


class TeamInput(BaseModel):
    guid: Optional[str] = Field(None)
    name: str = Field(None)
    color: str = Field(None)
    victories: int = Field(None)
    goals: int = Field(None)
    goals_negative: int = Field(None)
    guid_players: list = Field(None)

    class Config:
        orm_mode = True


class TeamOutput(BaseModel):
    guid: Optional[str] = Field(None)
    name: str = Field(None)
    color: str = Field(None)
    victories: int = Field(None)
    goals: int = Field(None)
    goals_negative: int = Field(None)
    players: List[PlayerOutput] = Field(None)

    class Config:
        orm_mode = True


class TeamUpdate(BaseModel):
    guid: Optional[str] = Field(None)
    name: str = Field(None)
    color: str = Field(None)
    victories: int = Field(None)
    goals: int = Field(None)
    goals_negative: int = Field(None)

    class Config:
        orm_mode = True
