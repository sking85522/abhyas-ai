from pydantic_settings import BaseSettings, SettingsConfigDict

class BaseAppSettings(BaseSettings):
    """Base configuration class that can be inherited by individual services."""
    env_name: str = "development"
    debug: bool = True

    # Common Database
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "admin"
    db_password: str = "secret"

    # Common JWT Secret
    jwt_secret: str = "super_secret_key"
    jwt_algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
