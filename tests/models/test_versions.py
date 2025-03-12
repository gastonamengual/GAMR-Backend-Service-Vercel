from gamr_backend_api_service.models.mlflow.versions import Versions


def test_dataset_valid() -> None:
    versions = Versions(versions=[1, 2])
    assert versions.versions == [1, 2]
