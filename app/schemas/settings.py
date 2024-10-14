from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    debug_log: bool = True
    echo_sql: bool = True

    class Config:
        env_file = "../.env"
