import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Page Object для главной страницы."""

    @allure.step('Кликнуть по кнопке "Заказать" в хедере')
    def click_order_button_header(self):
        """Кликает по кнопке 'Заказать' в хедере."""
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Кликнуть по кнопке "Заказать" в середине страницы')
    def click_order_button_middle(self):
        """Кликает по кнопке 'Заказать' в середине страницы."""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step('Кликнуть по кнопке "Заказать": {location}')
    def click_order_button(self, location):
        """Кликает по кнопке 'Заказать'.
        location: 'header' — кнопка в хедере, 'middle' — кнопка в середине страницы.
        """
        if location == 'header':
            self.click_order_button_header()
        elif location == 'middle':
            self.click_order_button_middle()
        else:
            raise ValueError(f"Неизвестная локация кнопки: {location}")

    @allure.step('Проскроллить до блока "Вопросы о важном"')
    def scroll_to_questions(self):
        """Скроллит страницу до блока 'Вопросы о важном'."""
        self.scroll_to_element(MainPageLocators.question_locator(0))

    @allure.step('Кликнуть по вопросу №{index}')
    def click_question(self, index):
        """Кликает по вопросу с указанным индексом."""
        self.scroll_to_questions()
        self.click_element(MainPageLocators.question_locator(index))

    @allure.step('Получить текст ответа №{index}')
    def get_answer_text(self, index):
        """Возвращает текст ответа с указанным индексом."""
        return self.get_text(MainPageLocators.answer_locator(index))
    