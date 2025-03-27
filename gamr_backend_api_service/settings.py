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

    PROJECT_ID: str = Field(default="")
    PRIVATE_KEY_ID: str = Field(default="")
    PRIVATE_KEY: str = Field(default="")
    CLIENT_EMAIL: str = Field(default="")
    CLIENT_ID: str = Field(default="")

    RENDER_API_TOKEN: str = Field(default="")

    JWT_KEY: str = Field(default="")
    JWT_ALGORITHM: str = Field(default="")

    FLOWER_API_BASE_URL: str = Field(default="")


Settings = Settings_()
