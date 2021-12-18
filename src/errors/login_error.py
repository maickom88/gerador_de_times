from src import ApiBaseException


class LoginException(ApiBaseException):
    status_code = 401

    def __init__(self, detail=None) -> None:
        self.detail = detail
        ApiBaseException.__init__(self, status_code=self.status_code, detail=self.detail)
