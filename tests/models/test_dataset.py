from gamr_backend_api_service.models.mlflow.dataset import Dataset


def test_dataset_valid() -> None:
    dataset = Dataset(X=[[1, 2, 3, 4]], y=[1])
    assert dataset.X == [[1, 2, 3, 4]]
    assert dataset.y == [1]


def test_flower_payload_default_y() -> None:
    dataset = Dataset(X=[[1, 2, 3, 4]])
    assert dataset.X == [[1, 2, 3, 4]]
    assert dataset.y is None
