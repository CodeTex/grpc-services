from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Gateway API"

    server_host: str = "0.0.0.0"
    server_port: int = 8050

    api_v1_str: str = ""


@lru_cache
def get_settings():
    return Settings()
