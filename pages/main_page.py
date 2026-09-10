from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Page Object для главной страницы."""

    def click_order_button_header(self):
        """Кликает по кнопке 'Заказать' в хедере."""
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_middle(self):
        """Кликает по кнопке 'Заказать' в середине страницы."""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element(MainPageLocators.ORDER_BUTTON_MIDDLE)

    def scroll_to_questions(self):
        """Скроллит страницу до блока 'Вопросы о важном'."""
        self.scroll_to_element(MainPageLocators.question_locator(0))

    def click_question(self, index):
        """Кликает по вопросу с указанным индексом."""
        self.scroll_to_questions()
        self.click_element(MainPageLocators.question_locator(index))

    def get_answer_text(self, index):
        """Возвращает текст ответа с указанным индексом."""
        return self.get_text(MainPageLocators.answer_locator(index))