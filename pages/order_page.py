import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа."""

    @allure.step('Заполнить первую форму заказа')
    def fill_first_form(self, name, surname, address, metro, phone):
        """Заполняет первую форму заказа."""
        self.send_keys(OrderPageLocators.INPUT_NAME, name)
        self.send_keys(OrderPageLocators.INPUT_SURNAME, surname)
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)
        self.send_keys(OrderPageLocators.INPUT_METRO, metro)
        self.click_element(OrderPageLocators.metro_station_option(metro))
        self.send_keys(OrderPageLocators.INPUT_PHONE, phone)
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Выбрать цвет самоката: {color}')
    def select_color(self, color):
        """Выбирает цвет самоката по его названию."""
        self.click_element(OrderPageLocators.color_checkbox(color))

    @allure.step('Заполнить вторую форму заказа')
    def fill_second_form(self, when, period, color, comment):
        """Заполняет вторую форму заказа."""
        self.send_keys(OrderPageLocators.INPUT_WHEN, when)
        self.click_element(OrderPageLocators.INPUT_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.rental_period_option(period))
        self.select_color(color)
        self.send_keys(OrderPageLocators.INPUT_COMMENT, comment)
        self.click_element(OrderPageLocators.BUTTON_ORDER)
        self.click_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)

    @allure.step('Получить текст сообщения об успешном заказе')
    def get_success_message(self):
        """Возвращает текст сообщения об успешном заказе."""
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_MESSAGE)
    