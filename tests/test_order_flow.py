import allure
import pytest
from data import BASE_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
class TestOrderFlow:
    """Тесты для позитивного сценария заказа самоката."""

    @allure.story('Позитивный сценарий заказа')
    @allure.title('Заказ через кнопку "{order_button}" с данными: {customer_info[name]}')
    @pytest.mark.parametrize('order_button, customer_info, rental_info', [
        (
            'header',
            {'name': 'Иван', 'surname': 'Петров', 'address': 'ул. Ленина, 1',
             'metro': 'Черкизовская', 'phone': '89001234567'},
            {'when': '01.01.2024', 'period': 'двое суток',
             'color': 'black', 'comment': 'Привет!'}
        ),
        (
            'middle',
            {'name': 'Мария', 'surname': 'Иванова', 'address': 'пр. Мира, 10',
             'metro': 'Сокольники', 'phone': '89007654321'},
            {'when': '05.01.2024', 'period': 'трое суток',
             'color': 'grey', 'comment': 'Позвоните за час'}
        )
    ])
    def test_successful_order(self, driver, order_button, customer_info, rental_info):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.click_order_button(order_button)

        order_page = OrderPage(driver)
        order_page.fill_first_form(
            customer_info['name'],
            customer_info['surname'],
            customer_info['address'],
            customer_info['metro'],
            customer_info['phone']
        )
        order_page.fill_second_form(
            rental_info['when'],
            rental_info['period'],
            rental_info['color'],
            rental_info['comment']
        )

        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text, \
            f"Сообщение об успешном заказе не появилось. Получено: '{success_text}'"
            