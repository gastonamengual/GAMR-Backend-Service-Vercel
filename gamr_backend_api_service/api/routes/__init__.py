from .auth import router as auth_router
from .base import router as home_router
from .exception_handlers import ERROR_TO_HANDLER_MAPPING
from .flower import router as flower_router
from .metrics import router as metrics_router
from .object import router as object_router

ROUTERS = [home_router, flower_router, object_router, metrics_router, auth_router]

__all__ = ["ERROR_TO_HANDLER_MAPPING", "ROUTERS"]
