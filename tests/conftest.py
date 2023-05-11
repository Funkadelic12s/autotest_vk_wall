from selenium import webdriver
import pytest


# Распаковка и настройки драйвера
@pytest.fixture()
def driver():
    driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
    yield driver
    driver.quit()
