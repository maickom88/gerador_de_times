from fastapi import APIRouter

from src.models.draw_model import DrawInput
from src.services.draw_service import DrawService
from src.settings.logger import logger

router = APIRouter()
draw_router = {
    "router": router,
    "prefix": "/draw",
    "tags": ["Draw"],
}


@router.post(path="",  status_code=201)
async def register_draw(draw: DrawInput):
    logger.info("Starting request to register_draw")
    service = DrawService()
    return await service.draw_players(draw)

