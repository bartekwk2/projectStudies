from datetime import datetime, timedelta
import bcrypt
import jwt
import csv

from .models.user import User
import os
from .helpers import get_token_from_header

from .exceptions import (
    InvalidCredentialsError,
    TokenExpiredError,
    InvalidTokenError,
    InvalidFieldError,
)


ENCODING = "utf-8"
USER_DATA = "data/users.csv"


def authenticate_user():
    token = get_token_from_header()
    if not token:
        raise InvalidTokenError()

    token_payload = decode_auth_token(token)

    current_user = get_user(token_payload["sub"])
    if not current_user:
        raise InvalidTokenError()


def get_user(user_email):
    with open(USER_DATA) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            email, password = row
            if email == user_email:
                return User(email, password)


def login_user(email, password):
    saved_user = get_user(email)
    if saved_user and check_password(password, saved_user.password):
        token = encode_auth_token(saved_user.email)
        return token
    else:
        raise InvalidCredentialsError()


def create_user(email, password):
    email_used = get_user(email)
    if email_used:
        raise InvalidFieldError("email", "Email jest w użyciu")

    hashed_password = hash_password(password)

    with open(USER_DATA, 'a', encoding=ENCODING, newline='') as f:
        writer = csv.writer(f)
        writer.writerow((email, hashed_password))


def hash_password(password):
    return bcrypt.hashpw(password.encode(ENCODING), bcrypt.gensalt()).decode(ENCODING)


def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(ENCODING), hashed_password.encode(ENCODING))


def encode_auth_token(user_mail):
    exp_days = int(os.getenv("AUTH_TOKEN_EXPIRATION_DAYS"))
    exp_seconds = int(os.getenv("AUTH_TOKEN_EXPIRATION_SECONDS"))
    exp_date = datetime.now() + timedelta(days=exp_days, seconds=exp_seconds)
    payload = {"exp": exp_date, "iat": datetime.today(), "sub": user_mail}
    return jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")


def decode_auth_token(token):
    try:
        payload = jwt.decode(token, os.getenv(
            "SECRET_KEY"), algorithms="HS256")
        return payload
    except jwt.ExpiredSignatureError as ex:
        raise TokenExpiredError() from ex
    except jwt.InvalidTokenError as ex:
        raise InvalidTokenError() from ex
