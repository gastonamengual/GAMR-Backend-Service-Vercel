from collections.abc import Generator
from unittest.mock import MagicMock, Mock, patch

import pytest

from gamr_backend_api_service.database_connector import FirestoreConnector
from gamr_backend_api_service.models.user import User


@pytest.fixture
def mock_firestore() -> Generator[tuple[MagicMock, MagicMock], None, None]:
    with (
        patch("firebase_admin.get_app", side_effect=ValueError),
        patch("firebase_admin.initialize_app") as mock_init,
        patch("firebase_admin.credentials.Certificate") as mock_cert,
    ):
        yield mock_init, mock_cert


@pytest.fixture
def firestore_connector(
    mock_firestore: Generator[tuple[MagicMock, MagicMock], None, None],  # noqa: ARG001
) -> FirestoreConnector:
    return FirestoreConnector()


@patch.object(FirestoreConnector, "_db")
def test_add_user(mock_db: MagicMock, firestore_connector: FirestoreConnector) -> None:
    mock_collection = Mock()
    mock_document = Mock()

    mock_db.collection.return_value = mock_collection
    mock_collection.document.return_value = mock_document

    firestore_connector.add_user("test_user")

    mock_db.collection.assert_called_once_with("users")
    mock_collection.document.assert_called_once()
    mock_document.set.assert_called_once_with({"username": "test_user"})


@patch.object(FirestoreConnector, "_db")
def test_get_all_users(
    mock_db: MagicMock, firestore_connector: FirestoreConnector
) -> None:
    mock_collection = Mock()
    mock_db.collection.return_value = mock_collection

    mock_doc_1 = Mock()
    mock_doc_1.to_dict.return_value = {"username": "user1"}

    mock_doc_2 = Mock()
    mock_doc_2.to_dict.return_value = {"username": "user2"}

    mock_collection.stream.return_value = [mock_doc_1, mock_doc_2]

    users = firestore_connector.get_all_users()

    assert len(users) == 2
    assert users[0] == User(username="user1")
    assert users[1] == User(username="user2")

    mock_db.collection.assert_called_once_with("users")
    mock_collection.stream.assert_called_once()


@patch("firebase_admin.get_app", side_effect=ValueError)
@patch("firebase_admin.initialize_app")
@patch(
    "gamr_backend_api_service.database_connector.firebase.get_credentials",
    return_value={"mock": "credentials"},
)
@patch("firebase_admin.credentials.Certificate")
def test_firestore_connector_initialization_new_app(
    mock_certificate: Mock,
    mock_get_credentials: Mock,  # noqa: ARG001
    mock_init_app: Mock,
    mock_get_app: Mock,  # noqa: ARG001
) -> None:
    mock_cred_instance = MagicMock()
    mock_certificate.return_value = mock_cred_instance

    FirestoreConnector()

    mock_certificate.assert_called_once_with({"mock": "credentials"})
    mock_init_app.assert_called_once_with(mock_cred_instance)
