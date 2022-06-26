import json
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

import firebase_admin
from firebase_admin import auth, credentials, messaging
from firebase_admin import storage
from fastapi import UploadFile
from firebase_admin.messaging import Notification

from src.errors.login_error import LoginException
from src.models.notification_model import NotificationInput
from src.services.device_service import DeviceService
from src.services.user_service import UserService
from src.settings.environment import env
from src.settings.logger import logger


class FirebaseAdminService:
    cred = credentials.Certificate(json.loads(env.firebase_account_credential()))
    _firebase_app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'gerador-de-time.appspot.com'
    })

    def __init__(self):
        self.bucket = storage.bucket()
        self.user_service = UserService()
        self.device_service = DeviceService()

    async def send_multicast(self, notification_input: NotificationInput):
        registration_tokens = await self.device_service.get_tokens()
        if len(registration_tokens) > 0:
            message = messaging.MulticastMessage(
                notification=Notification(
                    title=notification_input.title,
                    body=notification_input.description
                ),
                data=notification_input.data,
                tokens=registration_tokens,
            )
            response = messaging.send_multicast(message)
            return response
        return

    @staticmethod
    def validate_token(id_token: str) -> bool:
        try:
            decoded_token = auth.verify_id_token(id_token)
            if decoded_token.get("uid"):
                email = decoded_token.get("email")
                logger.info(f"Request authorized by {email}")
                return True
            return False
        except Exception as e:
            raise LoginException(detail=f"Invalid token: {e}")

    @staticmethod
    def get_uid(token: str) -> bool:
        try:
            decoded_token = auth.verify_id_token(token)
            if decoded_token.get("uid"):
                return decoded_token.get("uid")
            return False
        except Exception as e:
            raise LoginException(detail=f"Invalid token: {e}")

    @staticmethod
    def get_user(uid: str):
        return auth.get_user(uid)

    @staticmethod
    def revoke_refresh_tokens(uid: str):
        auth.revoke_refresh_tokens(uid)

    def get_images(self, name_file: str, email: str = None):
        if email is None:
            blob = self.bucket.blob(name_file)
            blob.make_public()
            return {"your file url": blob.public_url}
        blob = self.bucket.blob(f'{email}/{name_file}')
        blob.make_public()
        return {"your file url": blob.public_url}
    
    @staticmethod
    def save_upload_file_tmp(upload_file: UploadFile) -> Path:
        try:
            suffix = Path(upload_file.filename).suffix
            with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                shutil.copyfileobj(upload_file.file, tmp)
                tmp_path = Path(tmp.name)
        finally:
            upload_file.file.close()
        return tmp_path

    def upload_image(self, file: UploadFile, email: str = None):
        tmp_path = self.save_upload_file_tmp(file)
        bucket = storage.bucket()
        if email is None:
            blob = bucket.blob(file.filename)
        else:
            blob = bucket.blob(f'{email}/{file.filename}')
        blob.upload_from_filename(tmp_path)
        blob.make_public()

        return {"your file url": blob.public_url}

    async def delete_user(self, user_guid):
        user = await self.user_service.get_entity_by_guid(user_guid)
        if user.firebase_uid:
            auth.delete_user(user.firebase_uid)
        return True
