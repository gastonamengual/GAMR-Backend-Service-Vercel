from fastapi import APIRouter

from gamr_backend_api_service.auth import TokenGenerator
from gamr_backend_api_service.models.user import User
from gamr_backend_api_service.monitoring import PROMETHEYS_MONITOR

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "access the /detect_objects endpoint"}


@router.post("/token")
async def token(
    user: User,
) -> dict[str, str]:
    start_time = PROMETHEYS_MONITOR.start_time()

    token_generator = TokenGenerator()
    token_ = token_generator.get_token(user)

    duration = PROMETHEYS_MONITOR.get_duration(start_time)
    PROMETHEYS_MONITOR.observe_request(
        method="GET", endpoint="/token", duration=duration
    )
    return {"token": token_, "type": "BEARER"}
