from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    """Page Object для главной страницы effective-mobile.ru"""
    
    # Локаторы
    LOGO = "a.header__logo"
    NAVIGATION_MENU = "nav.header__nav"
    ABOUT_US_LINK = "a[href='#about']"
    CONTACTS_LINK = "a[href='#contacts']"
    SERVICES_LINK = "a[href='#services']"
    PORTFOLIO_LINK = "a[href='#portfolio']"
    
    # Секции
    ABOUT_SECTION = "#about"
    CONTACTS_SECTION = "#contacts"
    SERVICES_SECTION = "#services"
    PORTFOLIO_SECTION = "#portfolio"
    
    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        super().open("/")
        self.wait_for_load_state()
    
    @allure.step("Проверить видимость логотипа")
    def is_logo_visible(self) -> bool:
        """Проверить видимость логотипа"""
        return self.is_visible(self.LOGO)
    
    @allure.step("Проверить видимость навигации")
    def is_navigation_visible(self) -> bool:
        """Проверить видимость навигационного меню"""
        return self.is_visible(self.NAVIGATION_MENU)
    
    @allure.step("Перейти в раздел 'О нас'")
    def click_about_us(self):
        """Кликнуть на раздел 'О нас'"""
        self.click(self.ABOUT_US_LINK)
        self.wait_for_load_state()
    
    @allure.step("Проверить видимость раздела 'О нас'")
    def is_about_us_section_visible(self) -> bool:
        """Проверить видимость раздела 'О нас'"""
        return self.is_visible(self.ABOUT_SECTION)
    
    @allure.step("Перейти в раздел 'Контакты'")
    def click_contacts(self):
        """Кликнуть на раздел 'Контакты'"""
        self.click(self.CONTACTS_LINK)
        self.wait_for_load_state()
    
    @allure.step("Проверить видимость раздела 'Контакты'")
    def is_contacts_section_visible(self) -> bool:
        """Проверить видимость раздела 'Контакты'"""
        return self.is_visible(self.CONTACTS_SECTION)
    
    @allure.step("Перейти в раздел 'Услуги'")
    def click_services(self):
        """Кликнуть на раздел 'Услуги'"""
        self.click(self.SERVICES_LINK)
        self.wait_for_load_state()
    
    @allure.step("Проверить видимость раздела 'Услуги'")
    def is_services_section_visible(self) -> bool:
        """Проверить видимость раздела 'Услуги'"""
        return self.is_visible(self.SERVICES_SECTION)
