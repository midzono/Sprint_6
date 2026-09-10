from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа."""

    def fill_first_form(self, name, surname, address, metro, phone):
        """Заполняет первую форму заказа."""
        self.send_keys(OrderPageLocators.INPUT_NAME, name)
        self.send_keys(OrderPageLocators.INPUT_SURNAME, surname)
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)
        self.send_keys(OrderPageLocators.INPUT_METRO, metro)
        self.click_element(OrderPageLocators.metro_station_option(metro))
        self.send_keys(OrderPageLocators.INPUT_PHONE, phone)
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    def fill_second_form(self, when, period, color, comment):
        """Заполняет вторую форму заказа."""
        self.send_keys(OrderPageLocators.INPUT_WHEN, when)
        self.click_element(OrderPageLocators.INPUT_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.rental_period_option(period))
        if color == "black":
            self.click_element(OrderPageLocators.CHECKBOX_COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.CHECKBOX_COLOR_GREY)
        self.send_keys(OrderPageLocators.INPUT_COMMENT, comment)
        self.click_element(OrderPageLocators.BUTTON_ORDER)
        self.click_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)

    def get_success_message(self):
        """Возвращает текст сообщения об успешном заказе."""
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_MESSAGE)