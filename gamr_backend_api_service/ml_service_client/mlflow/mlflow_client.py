from dataclasses import dataclass

import requests

from gamr_backend_api_service.ml_service_client import AbstractMLServiceClient
from gamr_backend_api_service.models.mlflow import FlowerPayload, Models, Versions
from gamr_backend_api_service.settings import Settings

from .errors import MLFlowException


@dataclass
class FlowerClassifier(AbstractMLServiceClient):
    model_api_url: str = Settings.FLOWER_API_BASE_URL

    def predict(self, payload: FlowerPayload) -> FlowerPayload:
        try:
            url = f"{self.model_api_url}/model/{payload.model_name}/{payload.model_version}/predict"  # noqa: E501
            response = requests.post(url, json=payload.data.model_dump())

        except Exception as ex:
            raise MLFlowException(message=f"MLFLow API Error: {ex}") from ex

        payload.data.y = [response.json()["prediction"]]
        return payload

    def train(self, payload: FlowerPayload) -> FlowerPayload:
        try:
            url = f"{self.model_api_url}/model/{payload.model_name}/train"
            response = requests.post(url, json=payload.data.model_dump())

        except Exception as ex:
            raise MLFlowException(message=f"MLFLow API Error: {ex}") from ex

        payload.model_version = response.json()["model_version"]
        return payload

    def get_models(self) -> Models:
        try:
            url = f"{self.model_api_url}/model"
            response = requests.get(url)
            return Models(**response.json())

        except Exception as ex:
            raise MLFlowException(message=f"MLFLow API Error: {ex}") from ex

    def get_model_versions(self, model_name: str) -> Versions:
        try:
            url = f"{self.model_api_url}/model/{model_name}/versions"
            response = requests.get(url)
            return Versions(**response.json())

        except Exception as ex:
            raise MLFlowException(message=f"MLFLow API Error: {ex}") from ex
