from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from src.models.goal_player_model import GoalPlayerOutput
from src.models.player_model import PlayerOutput
from src.models.team_model import TeamOutput


class CupInforamtionOutput(BaseModel):
    winner: Optional[TeamOutput] = Field(None)
    best_player: Optional[GoalPlayerOutput] = Field(None)
    worst_team: Optional[TeamOutput] = Field(None)
    goalkeeper: Optional[PlayerOutput] = Field(None)
    created_at: datetime = Field(None)

