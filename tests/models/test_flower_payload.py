import pytest

from gamr_backend_api_service.models.mlflow.dataset import Dataset
from gamr_backend_api_service.models.mlflow.flower_payload import FlowerPayload


@pytest.fixture
def dataset() -> Dataset:
    return Dataset(X=[[]], y=[])


def test_flower_payload_valid(dataset: Dataset) -> None:
    payload = FlowerPayload(data=dataset, model_name="test_model", model_version="1")
    assert payload.data == dataset
    assert payload.model_name == "test_model"
    assert payload.model_version == "1"


def test_flower_payload_default_model_version(dataset: Dataset) -> None:
    payload = FlowerPayload(data=dataset, model_name="test_model")
    assert payload.model_version == ""
