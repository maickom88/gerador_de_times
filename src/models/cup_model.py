from typing import List, Optional
from pydantic import BaseModel, Field

from src.models.sport_model import SportOutput
from src.models.team_model import TeamOutput


class CupInput(BaseModel):
    guid: Optional[str] = Field(None)
    responsible_email: str = Field(None)
    time: int = Field(None)
    time_additions: int = Field(None)
    guid_sport: str = Field(None)
    guid_teams: list = Field(None)
    is_draft: bool = Field(None)

    class Config:
        orm_mode = True


class CupOutput(BaseModel):
    guid: Optional[str] = Field(None)
    responsible_email: str = Field(None)
    time: int = Field(None)
    time_additions: int = Field(None)
    sport: SportOutput = Field(None)
    winner: Optional[TeamOutput] = Field(None)
    is_draft: bool = Field(None)
    teams: List[TeamOutput] = Field(None)

    class Config:
        orm_mode = True
