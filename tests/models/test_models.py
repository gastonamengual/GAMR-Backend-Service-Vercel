from gamr_backend_api_service.models.mlflow.models import Models


def test_dataset_valid() -> None:
    models = Models(models=["model1", "model2"])
    assert models.models == ["model1", "model2"]
