from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL : str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    REDIS_URL:str
    MAIL_USERNAME:str
    MAIL_PASSWORD:str 
    MAIL_FROM :str
    MAIL_PORT: int = 587
    MAIL_SERVER :str
    MAIL_FROM_NAME:str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS:bool = True
    DOMAIN:str

    #Every class that is a pydantic model is going to have model_config
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = Settings()

broker_url = Config.REDIS_URL
result = Config.REDIS_URL
broker_connection_retry_on_startup = True