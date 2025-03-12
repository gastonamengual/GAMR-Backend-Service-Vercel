import pytest

from gamr_backend_api_service.ml_service_client import FlowerClassifier
from gamr_backend_api_service.models.mlflow import Dataset, FlowerPayload


@pytest.mark.vcr
def test_flower_classifier_predict() -> None:
    # Arrange
    classifier = FlowerClassifier(model_api_url="http://localhost:8084")
    payload = FlowerPayload(
        model_name="model_name",
        model_version="1",
        data=Dataset(X=[[5.1, 3.5, 1.4, 0.2]]),
    )

    result = classifier.predict(payload)

    assert result.data.y is not None
    assert isinstance(result.data.y, list)
