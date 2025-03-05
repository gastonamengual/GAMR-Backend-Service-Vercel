from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings_(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
        secrets_dir="secrets",
        extra="ignore",
    )

    PROJECT_ID: str = Field()
    PRIVATE_KEY_ID: str = Field()
    PRIVATE_KEY: str = Field()
    CLIENT_EMAIL: str = Field()
    CLIENT_ID: str = Field()


Settings = Settings_()
