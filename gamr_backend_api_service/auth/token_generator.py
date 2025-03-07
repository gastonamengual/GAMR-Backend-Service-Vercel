from dataclasses import dataclass
from datetime import datetime, timedelta

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from gamr_backend_api_service.auth.exceptions import (
    TokenNotDecoded,
)
from gamr_backend_api_service.models.user import User
from gamr_backend_api_service.settings import Settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@dataclass
class TokenGenerator:
    expiration_minutes: timedelta = timedelta(minutes=30)
    key: str = Settings.JWT_KEY
    algorithm: str = Settings.JWT_ALGORITHM

    @property
    def expire_data(self) -> datetime:
        return datetime.now() + self.expiration_minutes

    def get_token(self, user: User) -> str:
        payload = {"username": user.username, "exp": self.expire_data}
        return jwt.encode(payload=payload, key=self.key, algorithm=self.algorithm)

    def get_user_from_token(self, token: str = Depends(oauth2_scheme)) -> User:
        try:
            payload = jwt.decode(token, self.key, algorithms=[self.algorithm])
            return User(username=payload.get("username"))
        except Exception as exc:
            raise TokenNotDecoded from exc
