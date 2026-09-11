import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Object. Содержит общие методы."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Найти элемент по локатору: {locator}')
    def find_element(self, locator):
        """Находит элемент и ждёт его появления."""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Кликнуть по элементу: {locator}')
    def click_element(self, locator):
        """Кликает по элементу, дожидаясь его кликабельности."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Получить текст элемента: {locator}')
    def get_text(self, locator):
        """Возвращает текст элемента, дожидаясь его видимости."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step('Ввести текст "{text}" в поле: {locator}')
    def send_keys(self, locator, text):
        """Вводит текст в поле."""
        self.find_element(locator).send_keys(text)

    @allure.step('Проскроллить до элемента: {locator}')
    def scroll_to_element(self, locator):
        """Скроллит страницу до элемента."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_window(self):
        """Переключается на новую вкладку/окно."""
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        """Возвращает текущий URL."""
        return self.driver.current_url
    