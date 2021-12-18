
from src.controllers.user_controller import user_router


def get_routers() -> list:
    return [
        user_router
    ]
