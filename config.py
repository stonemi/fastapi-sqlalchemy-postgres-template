from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = "Default app_name"
    ADMIN_EMAIL: str = "default@email.com"
    items_per_user: int = 50
    DATABASE_URL: str = ''

    class Config:
        env_file = ".env"


class DevSettings(Settings):
    """로컬 설정"""
    class Config:
        env_file = "dev.env"


class ProdSettings(Settings):
    """운영 설정"""
    class Config:
        env_file = "prod.env"


class loadSetting:
    """설정 로드"""
    def __init__(self):
        # 현재 설정을 나타내는 field
        # 환경변수 MODE를 읽는다. 없으면 default dev로 설정
        self.mode = os.getenv("MODE", "dev")

    def __call__(self):
        if self.mode == "dev":
            return DevSettings()

        elif self.mode == "prod":
            return ProdSettings()

settings = Settings()