from fastapi.params import Security
from fastapi.security import APIKeyHeader
from fastapi.routing import Request

from src.errors.login_error import LoginException
from src.services.firebase_admin_service import FirebaseAdminService

x_api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def get_token(req: Request, api_key_header: str = Security(x_api_key_header)):
    pass
#    if req.method != 'GET':
#        if not api_key_header:
#            raise LoginException(detail="Bearer token is required")
#        if not FirebaseAdminService.validate_token(api_key_header):
#            raise LoginException(detail="Invalid token")
