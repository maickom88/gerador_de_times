from typing import Optional
from pydantic import BaseModel, Field

from src.models.match_model import MatchOutput
from src.models.player_model import PlayerOutput


class GoalInput(BaseModel):
    guid: Optional[str] = Field(None)
    time_goals: str = Field(None)
    guid_player: Optional[str] = Field(None)
    guid_macth: Optional[str] = Field(None)

    class Config:
        orm_mode = True


class GoalOutput(BaseModel):
    guid: Optional[str] = Field(None)
    player: PlayerOutput = Field(None)
    game: MatchOutput = Field(None)
    time_goals: str = Field(None)

    class Config:
        orm_mode = True
