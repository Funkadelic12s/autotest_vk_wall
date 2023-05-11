from selenium.webdriver.common.by import By


# Локаторы для поиска элементов на странице
class Locator:

    # Логин для авторизации
    login_name = ('id', "index_email")
    login_name_ent = (By.CLASS_NAME, "FlatButton.FlatButton--primary.FlatButton--size-l.Flat"
                                     "Button--wide.VkIdForm__button.VkIdForm__signInButton")

    # Пароль для авторизации
    password = ('name', 'password')
    password_ent = (By.CLASS_NAME, "vkuiButton.vkuiButton--sz-l.vkuiButton--lvl-primary.vkuiButton--clr-accent."
                                   "vkuiButton--aln-center.vkuiButton--sizeY-compact.vkuiButton--stretched.vkui"
                                   "Tappable.vkuiTappable--sizeX-regular.vkuiTappable--hasHover.vkuiTappable--mouse")
    # Моя страница
    my_page = ('id', "l_pr")

    # Мои записи
    my_posts = (By.CLASS_NAME, "_wall_tab_all")
    how_many_posts = (By.CLASS_NAME, "page_block_header_count")

    # Добавить запись
    post_field = ('id', "post_field")
    add_post = (By.CLASS_NAME, "addpost_button_wrap")
