from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gamr_backend_api_service.api.routes import ERROR_TO_HANDLER_MAPPING, ROUTERS


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    for router in ROUTERS:
        app.include_router(router)

    for error_exception, error_handler in ERROR_TO_HANDLER_MAPPING:
        app.add_exception_handler(error_exception, error_handler)  # type: ignore

    return app
