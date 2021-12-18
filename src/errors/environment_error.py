from src.errors.base_error import ApiBaseException


class EnvironmentException(ApiBaseException):
    status_code = 400

    def __init__(self, detail=None) -> None:
        self.detail = detail
        ApiBaseException.__init__(
            self, status_code=self.status_code, detail=self.detail)



