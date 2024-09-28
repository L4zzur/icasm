from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import FilePath, BaseModel


class UvicornConfig(BaseModel):
    """Settings for the Uvicorn server."""

    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    """Settings for the API v1 prefix."""

    prefix: str = "/api/v1"
    users: str = "/users"
    categories: str = "/categories"
    transactions: str = "/transactions"


class ApiPrefix(BaseModel):
    """Settings for the API prefix."""

    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    """Settings for the database."""

    file_path: FilePath
    echo: bool = False
    echo_pool: bool = False

    naming_conventions: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def url(self) -> str:
        return f"sqlite+aiosqlite:///{self.file_path}"


class Settings(BaseSettings):
    """Base settings for the project."""

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
    )
    app_mode: str = "dev"
    app_url: str = "localhost:8000"
    run: UvicornConfig = UvicornConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
