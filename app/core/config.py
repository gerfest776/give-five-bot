import decouple


class Settings:
    BOT_TOKEN: str = decouple.config("BOT_TOKEN")
    ADMIN: str = decouple.config("ADMIN")
    STAT_PATH: str = decouple.config("STAT_PATH")


settings = Settings()
