from selenium.webdriver.common.by import By


class HeaderPageLocators:
    """Локаторы хедера страницы."""
    LOGO_SCOOTER = [By.XPATH, "//img[@alt='Scooter']"]
    LOGO_YANDEX = [By.XPATH, "//img[@alt='Yandex']"]
    