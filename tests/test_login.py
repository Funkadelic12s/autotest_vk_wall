from pages.form_page import FormPage


# Тест авторизации
class TestVk:

    # Авторизуемся и сохраняем куки
    def test_vk_login(self, driver):
        vk = FormPage(driver, 'https://vk.com/')
        vk.open_url_login()
        print('Авторизация прошла успешна, файлы куки сохранены в файл "cooks"')
