from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    security_key: bytes  # 6hsjkJnsd)s-_=2$%723


settings = Settings()
