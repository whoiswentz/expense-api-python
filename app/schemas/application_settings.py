from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    database_url: PostgresDsn = Field(..., description="Database connection string in Postgres format")
    debug_log: bool = Field(True, description="Enable or disable debug logging")
    echo_sql: bool = Field(True, description="Log all SQL statements executed by SQLAlchemy")

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'
