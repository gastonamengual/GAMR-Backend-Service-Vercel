from fastapi import APIRouter, Depends, Response

from gamr_backend_api_service.auth import TokenGenerator
from gamr_backend_api_service.ml_service_client.hugging_face.hf_client import (
    HuggingFaceClient,
)
from gamr_backend_api_service.models.hugging_face import ImagePayload
from gamr_backend_api_service.models.user import User
from gamr_backend_api_service.services import UserManager

router = APIRouter()


@router.post("/detect_objects")
async def detect_objects(
    image_data: ImagePayload,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Response:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = HuggingFaceClient()
    image_data = model_interface.predict(payload=image_data)

    return image_data.response
