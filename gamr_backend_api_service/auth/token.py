from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from gamr_backend_api_service.auth.exceptions import (
    TokenNotDecoded,
)
from gamr_backend_api_service.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@dataclass
class TokenGenerator:
    expiration_minutes: timedelta = timedelta(minutes=30)
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"  # TODO save secret
    algorithm: str = "HS256"  # TODO save secret

    @property
    def expire_data(self):
        return datetime.now(timezone.utc) + self.expiration_minutes

    def get_token(self, user: User):
        payload = {"username": user.username, "exp": self.expire_data}
        token = jwt.encode(payload=payload, key=self.key, algorithm=self.algorithm)
        return token

    def get_user_from_token(self, token: str = Depends(oauth2_scheme)) -> User:
        try:
            payload = jwt.decode(token, self.key, algorithms=[self.algorithm])
            return User(username=payload.get("username"))
        except Exception as exc:
            raise TokenNotDecoded from exc
