import os


class Config:
    DB_NAME = os.getenv("PG_NAME") or "licensei"
    DB_USER = os.getenv("PG_USER") or "user"
    DB_PASSWORD = os.getenv("PG_PASSWORD") or "password"
    DB_HOST = os.getenv("PG_HOST") or "localhost"


# When more configs are added for other environments, add them to mapper too
config_mapper = {
    "default": Config
}
