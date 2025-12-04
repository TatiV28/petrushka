import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from utils.config import Config


@pytest.fixture(scope="session")
def browser_context():
    """Создание контекста браузера для всей сессии тестирования"""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=Config.HEADLESS,
            slow_mo=100 if not Config.HEADLESS else 0
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="ru-RU"
        )
        yield context
        context.close()
        browser.close()


@pytest.fixture
def page(browser_context):
    """Создание новой страницы для каждого теста"""
    page = browser_context.new_page()
    page.set_default_timeout(Config.TIMEOUT)
    yield page
    page.close()


@pytest.fixture
def main_page(page):
    """Фикстура для главной страницы"""
    return MainPage(page)
