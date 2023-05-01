import decouple


class Settings:
    BOT_TOKEN = decouple.config("BOT_TOKEN")
    ADMIN = decouple.config("ADMIN")


settings = Settings()
