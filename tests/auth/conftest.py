from datetime import datetime, timedelta

import jwt
import pytest

from gamr_backend_api_service.auth import TokenGenerator
from gamr_backend_api_service.models.user import User


@pytest.fixture
def key() -> str:
    return "secret"


@pytest.fixture
def algorithm() -> str:
    return "HS256"


@pytest.fixture
def token_generator(key: str, algorithm: str) -> TokenGenerator:
    return TokenGenerator(key=key, algorithm=algorithm)


@pytest.fixture
def user() -> User:
    return User(username="gaston")


@pytest.fixture
def token(user: User, algorithm: str, key: str) -> str:
    payload: dict[str, str | datetime] = {
        "username": user.username,
        "exp": datetime.now() + timedelta(30),
    }
    return jwt.encode(payload=payload, key=key, algorithm=algorithm)
