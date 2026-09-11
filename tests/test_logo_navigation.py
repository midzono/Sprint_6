import allure
from data import BASE_URL, DZEN_URL
from pages.main_page import MainPage
from pages.header_page import HeaderPage


@allure.feature('Навигация')
class TestLogoNavigation:
    """Тесты для проверки навигации по логотипам."""

    @allure.story('Проверка логотипа "Самокат"')
    @allure.title('Клик по логотипу "Самокат" ведёт на главную страницу')
    def test_logo_scooter_navigation(self, driver):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.click_order_button_header()

        header_page = HeaderPage(driver)
        header_page.click_logo_scooter()

        assert driver.current_url == BASE_URL, \
            "Клик по логотипу 'Самокат' не привёл на главную страницу"

    @allure.story('Проверка логотипа "Яндекс"')
    @allure.title('Клик по логотипу "Яндекс" открывает Дзен в новом окне')
    def test_logo_yandex_navigation(self, driver):
        driver.get(BASE_URL)
        header_page = HeaderPage(driver)
        header_page.click_logo_yandex()

        assert DZEN_URL in driver.current_url, \
            f"Редирект на Дзен не выполнен. Текущий URL: {driver.current_url}"
            