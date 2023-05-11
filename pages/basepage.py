import time
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from locators.locators import Locator
from keys.keys import Keys
import pickle


# Основной класс драйвера
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # Метод ожидания появления элемента на странице
    def visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    # Метод авторизации
    def open_url_login(self):
        self.driver.get(self.url)

        # Вводим email в окне авторизации
        login_name = self.visible(Locator.login_name)
        login_name.send_keys(Keys.email)
        self.visible(Locator.login_name_ent).click()

        # Пароль
        password = self.visible(Locator.password)
        password.send_keys(Keys.password)
        self.visible(Locator.password_ent).click()
        time.sleep(5)

        # Сохраняем сессию
        pickle.dump(self.driver.get_cookies(), open('cooks', 'wb'))

    # Метод загрузки куки
    def load(self):
        # Переходим по адрессу страницы
        self.driver.get(self.url)
        time.sleep(4)

        # Загружаем файлы куки
        for cook in pickle.load(open('cooks', 'rb')):
            self.driver.add_cookie(cook)
        time.sleep(2)

        # Обновляем страницу
        self.driver.refresh()
        time.sleep(2)
