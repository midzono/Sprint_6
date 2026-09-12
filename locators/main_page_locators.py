from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы."""
    # Кнопки "Заказать"
    ORDER_BUTTON_HEADER = [By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"]
    ORDER_BUTTON_MIDDLE = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"]

    # Шаблоны локаторов для вопросов и ответов
    QUESTION_LOCATOR_TEMPLATE = "accordion__heading-{}"
    ANSWER_LOCATOR_TEMPLATE = "accordion__panel-{}"

    @staticmethod
    def question_locator(index):
        """Возвращает локатор для вопроса по его индексу."""
        return [By.ID, MainPageLocators.QUESTION_LOCATOR_TEMPLATE.format(index)]

    @staticmethod
    def answer_locator(index):
        """Возвращает локатор для ответа по его индексу."""
        return [By.ID, MainPageLocators.ANSWER_LOCATOR_TEMPLATE.format(index)]
    