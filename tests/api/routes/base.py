from fastapi import APIRouter, Depends, Response

from gamr_backend_api_service.auth.token_generator import TokenGenerator
from gamr_backend_api_service.model_registries import (
    ModelService,
    get_ai_model_interface,
)
from gamr_backend_api_service.models import ImageData, User
from gamr_backend_api_service.services.user_manager import UserManager

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "access the /detect_objects endpoint"}


@router.post("/token")
async def token(user: User) -> dict[str, str]:
    token_generator = TokenGenerator()
    token_ = token_generator.get_token(user)
    return {"token": token_, "type": "BEARER"}


@router.post("/detect_objects")
async def detect_objects(
    image_data: ImageData,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Response:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = get_ai_model_interface(ModelService[image_data.model_service])
    image_data = model_interface().predict(image_data=image_data)  # type: ignore

    return image_data.response
