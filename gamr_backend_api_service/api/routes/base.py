from typing import Annotated

from fastapi import APIRouter, Depends, Response

from gamr_backend_api_service.auth import TokenGenerator
from gamr_backend_api_service.ml_service_client import (
    FlowerClassifier,
)
from gamr_backend_api_service.ml_service_client.hugging_face.hf_client import (
    HuggingFaceClient,
)
from gamr_backend_api_service.models import FlowerPayload, ImagePayload, User
from gamr_backend_api_service.models.mlflow.payload import Models, Versions
from gamr_backend_api_service.services import UserManager

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
    image_data: ImagePayload,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Response:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = HuggingFaceClient()
    image_data = model_interface.predict(payload=image_data)

    return image_data.response


@router.post("/flower/specie/classify/")
async def predict_flower(
    payload: FlowerPayload,
    current_user: Annotated[User, Depends(TokenGenerator().get_user_from_token)],
    flower_classifier: Annotated[FlowerClassifier, Depends(FlowerClassifier)],
) -> FlowerPayload:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    return flower_classifier.predict(payload)


@router.post("/flower/specie/train")
async def train_flower(
    payload: FlowerPayload,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> FlowerPayload:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = FlowerClassifier()

    return model_interface.train(payload)


@router.get("/flower/specie/classifiers")
async def models(
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Models:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = FlowerClassifier()

    return model_interface.get_models()


@router.get("/flower/specie/{classifier}/versions")
async def model_versions(
    classifier: str,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Versions:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = FlowerClassifier()

    return model_interface.get_model_versions(model_name=classifier)
