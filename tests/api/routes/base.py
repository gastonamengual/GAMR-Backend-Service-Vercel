from fastapi import APIRouter

from gamr_backend_api_service.auth.token_generator import TokenGenerator
from gamr_backend_api_service.models import User

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "access the /detect_objects endpoint"}


@router.post("/token")
async def token(user: User) -> dict[str, str]:
    token_generator = TokenGenerator()
    token_ = token_generator.get_token(user)
    return {"token": token_, "type": "BEARER"}
