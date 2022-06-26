
from fastapi import APIRouter, Depends, UploadFile, File

from src.authenticator.auth import get_token
from src.services.firebase_admin_service import FirebaseAdminService
from src.settings.logger import logger

router = APIRouter()
storage_router = {
    "router": router,
    "prefix": "/storage",
    "tags": ["Storage"],
    "dependencies": [Depends(get_token)]
}


@router.get(path="")
async def get_storages(filename: str):
    logger.info("Starting request to get_storages")
    service = FirebaseAdminService()
    return service.get_images(filename)


@router.post(path="/upload")
async def upload_storage(file: UploadFile = File(...)):
    logger.info("Starting request to get_storages")
    service = FirebaseAdminService()
    return service.upload_image(file)

