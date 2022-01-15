from typing import List

from pydantic import BaseModel, Field

from src.models.player_model import PlayerOutput
from src.models.team_model import TeamOutput


class DrawInput(BaseModel):
    balance_teams: bool = Field(None)
    number_of_teams: int = Field(None)
    players: List[PlayerOutput] = Field(None)

    class Config:
        orm_mode = True


class CupOutput(BaseModel):
    balance_teams: bool = Field(None)
    number_of_teams: int = Field(None)
    teams: TeamOutput = Field(None)

    class Config:
        orm_mode = True
