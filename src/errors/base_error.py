from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.settings.logger import logger


class ApiBaseException(HTTPException):
    status_code = 500
    detail = "Error in the servant while accessing this route."

    def __init__(self, status_code=500, detail=None) -> None:
        self.status_code = status_code
        if detail is not None:
            self.detail = detail


async def generic_handler(_: Request, exception: ApiBaseException):
    logger.error(exception)
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.detail}
    )