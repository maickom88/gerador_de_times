from typing import Optional, List

from pydantic import BaseModel, Field

from src.models.goal_model import GoalOutput


class PerformaceOutput(BaseModel):
    total_number_of_cup_participations: int = Field(None)
    goals: Optional[List[GoalOutput]] = Field(None)
    total_winner_cups: int = Field(None)

