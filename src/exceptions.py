class KeyAlreadyExists(BaseException):
    status_code = 409


class KeyNotFound(BaseException):
    status_code = 404
