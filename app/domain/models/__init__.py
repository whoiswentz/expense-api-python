from functools import lru_cache

from .application_settings import ApplicationSettings


@lru_cache
def get_settings():
    return ApplicationSettings()
