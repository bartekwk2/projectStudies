from flask import jsonify


class AppError(Exception):

    status_code = 500
    error_code = "INTERNAL_ERROR"
    message = "Request nie może być przetworzony w tym momencie"

    def __init__(self, status_code=None, error_code=None, message=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        if error_code is not None:
            self.error_code = error_code

    def to_api_response(self):
        response = jsonify(
            {"errorCode": self.error_code, "errorMessage": self.message}
        )
        response.status_code = self.status_code
        return response

class InvalidNumberError(AppError):
    def __init__(self):
        AppError.__init__(
            self,
            status_code=400,
            error_code="INVALID_NUMBER",
            message="Podano wartość, która nie jest liczbą całkowitą",
        )

class InvalidCredentialsError(AppError):
    def __init__(self):
        AppError.__init__(
            self,
            status_code=401,
            error_code="INVALID_DATA",
            message="Nieprawidłowa nazwa użytkownika lub hasło",
        )

class InvalidTokenError(AppError):
    def __init__(self):
        AppError.__init__(
            self,
            status_code=401,
            error_code="INVALID_TOKEN",
            message="Token jest nieważny lub brak tokena",
        )

class TokenExpiredError(AppError):
    def __init__(self):
        AppError.__init__(
            self,
            status_code=401,
            error_code="TOKEN_EXPIRED",
            message="Token wygasł",
        )

class InvalidFieldError(AppError):
    def __init__(self, field_name, message=""):
        AppError.__init__(
            self,
            status_code=422,
            error_code="INVALID_FIELD",
            message=f"Nieprawidłowe pole: {field_name}. {message}",
        )

class BadRequestError(AppError):
    def __init__(self, message="Nieprawidłowe żądanie."):
        AppError.__init__(
            self, status_code=400, error_code="BAD_REQUEST", message=message
        )


class NotFoundError(AppError):
    def __init__(self, message="Nie znaleziono"):
        AppError.__init__(
            self, status_code=404, error_code="NOT_FOUND", message=message
        )