from datetime import datetime

import jwt
import pytest
from freezegun import freeze_time

from gamr_backend_api_service.auth import TokenGenerator
from gamr_backend_api_service.auth.exceptions import TokenNotDecoded
from gamr_backend_api_service.models.user import User


@freeze_time("2025-01-01 02:00:00")  # type: ignore
def test_expire(token_generator: TokenGenerator) -> None:
    expiration_date = token_generator.expire_data

    assert expiration_date == datetime(2025, 1, 1, 2, 30)


def test_get_token(
    user: User, token_generator: TokenGenerator, key: str, algorithm: str
) -> None:
    token = token_generator.get_token(user)
    decoded = jwt.decode(
        token, key, algorithms=[algorithm], options={"verify_exp": False}
    )
    assert decoded["username"] == user.username


def test_get_user_from_token(
    token: str, token_generator: TokenGenerator, user: User
) -> None:
    user = token_generator.get_user_from_token(token=token)
    assert user.username == user.username


def test_get_user_from_tokenerror(token_generator: TokenGenerator) -> None:
    with pytest.raises(TokenNotDecoded) as ex:  # noqa: PT012
        token_generator.get_user_from_token("")
        assert (
            str(ex.value)
            == "Authentication failed: could not decode JWT token correctly"
        )
