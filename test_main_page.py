import pytest
import allure
from pages.main_page import MainPage


@allure.feature("Главная страница")
@allure.story("Навигация")
class TestMainPage:
    
    @allure.title("Проверка перехода в раздел 'О нас'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_about_us_navigation(self, main_page):
        """Тест проверяет переход в раздел 'О нас'"""
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Нажать на раздел 'О нас'"):
            main_page.click_about_us()
        
        with allure.step("Проверить URL раздела"):
            assert main_page.is_about_us_section_visible(), "Раздел 'О нас' не отображается"
    
    @allure.title("Проверка перехода в раздел 'Контакты'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_contacts_navigation(self, main_page):
        """Тест проверяет переход в раздел 'Контакты'"""
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Нажать на раздел 'Контакты'"):
            main_page.click_contacts()
        
        with allure.step("Проверить отображение раздела контактов"):
            assert main_page.is_contacts_section_visible(), "Раздел 'Контакты' не отображается"
    
    @allure.title("Проверка перехода в раздел 'Услуги'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_services_navigation(self, main_page):
        """Тест проверяет переход в раздел 'Услуги'"""
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Нажать на раздел 'Услуги'"):
            main_page.click_services()
        
        with allure.step("Проверить отображение раздела услуг"):
            assert main_page.is_services_section_visible(), "Раздел 'Услуги' не отображается"
    
    @allure.title("Проверка всех элементов навигации")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_all_navigation_elements_present(self, main_page):
        """Тест проверяет наличие всех элементов навигации на главной странице"""
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Проверить наличие всех навигационных элементов"):
            assert main_page.is_navigation_visible(), "Навигация не отображается"
            
        with allure.step("Проверить логотип"):
            assert main_page.is_logo_visible(), "Логотип не отображается"
