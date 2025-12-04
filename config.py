import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Конфигурация проекта"""
    
    BASE_URL = os.getenv("BASE_URL", "https://effective-mobile.ru")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
