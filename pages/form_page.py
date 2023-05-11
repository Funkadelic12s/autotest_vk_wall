import time
from pages.basepage import BasePage
from locators.locators import Locator


class FormPage(BasePage):

    # Метод проверки колическтва записей на стене
    def zero_posts(self):
        # Загружаем страницу с файлами куки
        self.load()
        # Проверяем мои записи на странице
        self.visible(Locator.my_page).click()
        time.sleep(5)
        self.visible(Locator.my_posts).click()
        time.sleep(3)

        # Возвращаем количество записей на странице
        return self.visible(Locator.how_many_posts).text

    # Метод добавления новой записи на странице
    def post(self):
        # Загружаем страницу с файлами куки
        self.load()
        time.sleep(10)
        # Добавляем запись на страницу
        field = self.visible(Locator.post_field)
        field.send_keys('Hello, World')
        time.sleep(10)
        self.visible(Locator.add_post).click()
        time.sleep(5)

        # Проверяем мои записи на странице
        self.visible(Locator.my_page).click()
        time.sleep(10)
        self.visible(Locator.my_posts).click()
        time.sleep(1)
        self.visible(Locator.my_posts).click()
        time.sleep(5)

        # Возвращаем количество записей
        return self.visible(Locator.how_many_posts).text
