from dataclasses import dataclass, field

from gamr_backend_api_service.auth.exceptions import (
    UserNotExists,
)
from gamr_backend_api_service.database_connector import (
    AbstractDatabaseConnector,
    FirestoreConnector,
)
from gamr_backend_api_service.models.user import User


@dataclass
class UserManager:
    db_connector: AbstractDatabaseConnector = field(default_factory=FirestoreConnector)  # type: ignore

    def validate_user_exists(self, user: User) -> User:
        users = self.db_connector.get_all_users()
        user_exists = any(
            user for found_user in users if user.username == found_user.username
        )
        if not user_exists:
            raise UserNotExists
        return user
