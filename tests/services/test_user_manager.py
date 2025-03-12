from unittest.mock import MagicMock

import pytest

from gamr_backend_api_service.auth.exceptions import UserNotExists
from gamr_backend_api_service.database_connector.firebase import FirestoreConnector
from gamr_backend_api_service.models.user import User
from gamr_backend_api_service.services.user_manager import UserManager


@pytest.fixture
def mock_db_connector() -> MagicMock:
    return MagicMock(spec=FirestoreConnector)


@pytest.fixture
def user_manager(mock_db_connector: MagicMock) -> UserManager:
    return UserManager(db_connector=mock_db_connector)


def test_validate_user_exists_existing_user(
    user_manager: UserManager, mock_db_connector: MagicMock
) -> None:
    user = User(username="test_user")
    mock_db_connector.get_all_users.return_value = [
        User(username="test_user"),
        User(username="another_user"),
    ]

    found_user = user_manager.validate_user_exists(user)
    mock_db_connector.get_all_users.assert_called_once()
    assert user == found_user


def test_validate_user_exists_user_not_found(
    user_manager: UserManager, mock_db_connector: MagicMock
) -> None:
    user = User(username="nonexistent_user")
    mock_db_connector.get_all_users.return_value = [
        User(username="test_user"),
        User(username="another_user"),
    ]

    with pytest.raises(UserNotExists):
        user_manager.validate_user_exists(user)

    mock_db_connector.get_all_users.assert_called_once()
