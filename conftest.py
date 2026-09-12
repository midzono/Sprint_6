import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    """Фикстура для создания и закрытия драйвера Firefox."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()