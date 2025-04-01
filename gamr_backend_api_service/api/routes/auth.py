from fastapi import APIRouter

from gamr_backend_api_service.auth import TokenGenerator
from gamr_backend_api_service.models.user import User
from gamr_backend_api_service.monitoring import PROMETHEUS_MONITOR

router = APIRouter()


@router.post("/token")
async def token(
    user: User,
) -> dict[str, str]:
    PROMETHEUS_MONITOR.increase_num_requests("/token")

    token_generator = TokenGenerator()
    token_ = token_generator.get_token(user)

    return {"token": token_, "type": "BEARER"}
