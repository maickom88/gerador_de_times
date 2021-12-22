from src.controllers.cup_controller import cup_router
from src.controllers.player_controller import player_router
from src.controllers.position_controller import position_router
from src.controllers.skill_controller import skill_router
from src.controllers.sport_controller import sport_router
from src.controllers.team_controller import team_router
from src.controllers.user_controller import user_router


def get_routers() -> list:
    return [
        user_router,
        sport_router,
        player_router,
        skill_router,
        position_router,
        team_router,
        cup_router
    ]
