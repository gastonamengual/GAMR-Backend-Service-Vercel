from pydantic import BaseModel

from gamr_backend_api_service.models.mlflow.dataset import Dataset


class FlowerPayload(BaseModel):
    data: Dataset
    model_name: str
    model_version: str | None = ""
