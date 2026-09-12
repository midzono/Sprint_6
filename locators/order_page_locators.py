from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы оформления заказа."""
    # Первая форма
    INPUT_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    INPUT_SURNAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    INPUT_ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    INPUT_METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    INPUT_PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]

    # Вторая форма
    INPUT_WHEN = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    INPUT_RENTAL_PERIOD = [By.XPATH, "//div[@class='Dropdown-placeholder']"]
    INPUT_COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    BUTTON_ORDER = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]
    BUTTON_CONFIRM_ORDER = [By.XPATH, "//button[text()='Да']"]

    # Сообщение об успешном заказе
    ORDER_SUCCESS_MESSAGE = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]

    @staticmethod
    def metro_station_option(station_name):
        """Возвращает локатор для станции метро по её названию."""
        return [By.XPATH, f"//div[text()='{station_name}']"]

    @staticmethod
    def rental_period_option(period):
        """Возвращает локатор для периода аренды по его названию."""
        return [By.XPATH, f"//div[text()='{period}']"]

    @staticmethod
    def color_checkbox(color):
        """Возвращает локатор чекбокса цвета: 'black' или 'grey'."""
        return [By.ID, color]
    