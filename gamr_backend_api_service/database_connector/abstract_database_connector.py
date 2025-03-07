from abc import ABC, abstractmethod
from dataclasses import dataclass

from gamr_backend_api_service.models.user import User


@dataclass
class AbstractDatabaseConnector(ABC):
    @abstractmethod
    def add_user(self, username: str) -> None: ...

    @abstractmethod
    def get_all_users(self) -> list[User]: ...
