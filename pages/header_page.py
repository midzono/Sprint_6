from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    """Page Object для хедера страницы."""

    def click_logo_scooter(self):
        """Кликает по логотипу 'Самокат'."""
        self.click_element(HeaderPageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        """Кликает по логотипу 'Яндекс' и переключается на новую вкладку."""
        self.click_element(HeaderPageLocators.LOGO_YANDEX)
        self.switch_to_new_window()