from fastapi import HTTPException


class KeyAlreadyExists(HTTPException):
    status_code = 409


class KeyNotFound(HTTPException):
    status_code = 404
