from flask import request
from .exceptions import BadRequestError


def get_token_from_header():
    token = None
    if "Authorization" in request.headers:
        auth_header = request.headers["Authorization"]
        try:
            token = auth_header.split(" ")[1]
        except IndexError:
            token = None
    return token


def auth_data_check():
    if not request.json:
        raise BadRequestError()
    if not "email" in request.json:
        raise BadRequestError("Nie podano emaila")
    if not "password" in request.json:
        raise BadRequestError("Nie podano hasła")
