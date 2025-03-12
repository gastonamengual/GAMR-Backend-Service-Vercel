from typing import Never

import pytest

from gamr_backend_api_service.auth.exceptions import TokenNotDecoded, UserNotExists


def test_user_not_exists() -> None:
    msg = "User does not exist"

    def raise_user_not_exists(msg: str) -> Never:
        raise UserNotExists(msg)  # type: ignore

    with pytest.raises(UserNotExists, match=msg):
        raise_user_not_exists(msg)


def test_token_not_decoded() -> None:
    msg = "Token could not be decoded"

    def raise_token_not_decoded(msg: str) -> Never:
        raise TokenNotDecoded(msg)  # type: ignore

    with pytest.raises(TokenNotDecoded, match=msg):
        raise_token_not_decoded(msg)
