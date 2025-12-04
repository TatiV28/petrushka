from playwright.sync_api import Page
import allure
from utils.config import Config


class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = Config.BASE_URL
    
    @allure.step("Открыть URL: {url}")
    def open(self, url: str = ""):
        """Открыть страницу по URL"""
        full_url = f"{self.base_url}{url}"
        self.page.goto(full_url, wait_until="domcontentloaded")
    
    @allure.step("Кликнуть на элемент: {locator}")
    def click(self, locator: str):
        """Кликнуть на элемент"""
        self.page.click(locator)
    
    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator: str, timeout: int = 5000) -> bool:
        """Проверить видимость элемента"""
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            return True
        except:
            return False
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator: str) -> str:
        """Получить текст элемента"""
        return self.page.locator(locator).text_content()
    
    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        """Получить текущий URL"""
        return self.page.url
    
    @allure.step("Скроллить к элементу: {locator}")
    def scroll_to_element(self, locator: str):
        """Скроллить к элементу"""
        self.page.locator(locator).scroll_into_view_if_needed()
    
    @allure.step("Ожидать загрузки страницы")
    def wait_for_load_state(self, state: str = "networkidle"):
        """Ожидать определенного состояния загрузки"""
        self.page.wait_for_load_state(state)
