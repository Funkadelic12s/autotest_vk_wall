from pages.form_page import FormPage


# Тест стены вк
class TestVkWall:

    # Проверка изначального количества записей на стене вк
    def test_zero_post(self, driver):
        vk = FormPage(driver, 'https://vk.com/')
        assert vk.zero_posts() == '-1'

    # Проверка количества записей после публикации
    def test_post(self, driver):
        vk = FormPage(driver, 'https://vk.com/')
        assert vk.post() == '1'
