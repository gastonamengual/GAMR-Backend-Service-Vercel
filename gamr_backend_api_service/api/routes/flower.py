from typing import Annotated

from fastapi import APIRouter, Depends

from gamr_backend_api_service.auth import TokenGenerator
from gamr_backend_api_service.ml_service_client import (
    FlowerClassifier,
)
from gamr_backend_api_service.models.mlflow import FlowerPayload, Models, Versions
from gamr_backend_api_service.models.user import User
from gamr_backend_api_service.monitoring import PROMETHEUS_MONITOR
from gamr_backend_api_service.services import UserManager

router = APIRouter(prefix="/flower")


@router.post("/classify/")
async def predict_flower(
    payload: FlowerPayload,
    current_user: Annotated[User, Depends(TokenGenerator().get_user_from_token)],
    flower_classifier: Annotated[FlowerClassifier, Depends(FlowerClassifier)],
) -> FlowerPayload:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)

    start_time = PROMETHEUS_MONITOR.start_time()
    PROMETHEUS_MONITOR.increase_current_requests("/flower/classify/")

    result = flower_classifier.predict(payload)

    PROMETHEUS_MONITOR.record_request_duration(start_time, "/flower/classify/")
    PROMETHEUS_MONITOR.decrease_current_requests("/flower/classify/")

    return result


@router.post("/train")
async def train_flower(
    payload: FlowerPayload,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> FlowerPayload:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = FlowerClassifier()

    start_time = PROMETHEUS_MONITOR.start_time()
    PROMETHEUS_MONITOR.increase_current_requests("/flower/train/")

    result = model_interface.train(payload)

    PROMETHEUS_MONITOR.record_request_duration(start_time, "/flower/train/")
    PROMETHEUS_MONITOR.decrease_current_requests("/flower/train/")

    return result


@router.get("/classifiers")
async def models(
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Models:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = FlowerClassifier()

    start_time = PROMETHEUS_MONITOR.start_time()
    PROMETHEUS_MONITOR.increase_current_requests("/flower/classifiers/")

    result = model_interface.get_models()

    PROMETHEUS_MONITOR.record_request_duration(start_time, "/flower/classifiers/")
    PROMETHEUS_MONITOR.decrease_current_requests("/flower/classifiers/")

    return result


@router.get("/{classifier}/versions")
async def model_versions(
    classifier: str,
    current_user: User = Depends(TokenGenerator().get_user_from_token),
) -> Versions:
    user_manager = UserManager()
    user_manager.validate_user_exists(current_user)
    model_interface = FlowerClassifier()

    start_time = PROMETHEUS_MONITOR.start_time()
    PROMETHEUS_MONITOR.increase_current_requests("/classifier/versions/")

    result = model_interface.get_model_versions(model_name=classifier)

    PROMETHEUS_MONITOR.record_request_duration(start_time, "/classifier/versions/")
    PROMETHEUS_MONITOR.decrease_current_requests("/classifier/versions/")

    return result
