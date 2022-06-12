from typing import Optional

from pydantic import BaseModel, Field

from src.models.cup_model import CupOutput
from src.models.team_model import TeamOutput


class MatchInput(BaseModel):
    guid: Optional[str] = Field(None)
    guid_home_team: str = Field(None)
    guid_opposing_team: Optional[str] = Field(None)
    guid_cup: Optional[str] = Field(None)
    time: Optional[int] = Field(None)
    time_additions: Optional[int] = Field(None)

    class Config:
        orm_mode = True


class MatchUpdate(BaseModel):
    guid: Optional[str] = Field(None)
    total_time_pause: Optional[int] = Field(None)
    final_time: Optional[int] = Field(None)
    total_goals: Optional[int] = Field(None)

    class Config:
        orm_mode = True


class MatchOutput(BaseModel):
    guid: Optional[str] = Field(None)
    home_team: TeamOutput = Field(None)
    opposing_team: TeamOutput = Field(None)
    cup: CupOutput = Field(None)
    time: Optional[int] = Field(None)
    time_additions: Optional[int] = Field(None)
    total_time_pause: Optional[int] = Field(None)
    final_time: Optional[int] = Field(None)
    total_goals: Optional[int] = Field(None)

    class Config:
        orm_mode = True
