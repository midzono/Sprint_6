from selenium.webdriver.common.by import By


class BaseLocators:
    """Общие локаторы, которые могут использоваться на разных страницах."""
    # Логотипы в хедере
    LOGO_SCOOTER = [By.XPATH, "//img[@alt='Scooter']"]
    LOGO_YANDEX = [By.XPATH, "//img[@alt='Yandex']"]