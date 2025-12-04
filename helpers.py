import allure
from datetime import datetime


def attach_screenshot(page, name: str = "screenshot"):
    """Прикрепить скриншот к отчету Allure"""
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        attachment_type=allure.attachment_type.PNG
    )


def attach_page_source(page, name: str = "page_source"):
    """Прикрепить HTML код страницы к отчету Allure"""
    html = page.content()
    allure.attach(
        html,
        name=f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        attachment_type=allure.attachment_type.HTML
    )
