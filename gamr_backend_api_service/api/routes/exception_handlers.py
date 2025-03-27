from fastapi import Request
from fastapi.responses import JSONResponse

from gamr_backend_api_service.auth.exceptions import (
    TokenNotDecoded,
    UserNotExists,
)
from gamr_backend_api_service.ml_service_client import (
    HuggingFaceException,
)


def user_not_exists_exception_handler(
    request: Request,  # noqa: ARG001
    exc: UserNotExists,
) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


def token_not_decoded_exception_handler(
    request: Request,  # noqa: ARG001
    exc: TokenNotDecoded,
) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


def hugging_face_api_exception_handler(
    request: Request,  # noqa: ARG001
    exc: HuggingFaceException,
) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


ERROR_TO_HANDLER_MAPPING = [
    [UserNotExists, user_not_exists_exception_handler],
    [TokenNotDecoded, token_not_decoded_exception_handler],
    [HuggingFaceException, hugging_face_api_exception_handler],
]
