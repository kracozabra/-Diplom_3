import allure
from pages.base_page import BasePage
import locators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку страницы логина')
    def wait_for_load_login_page(self):
        self.wait_for_element_visible(locators.LOGIN_PAGE_HEADER)

    @allure.step('Кликаем на кнопку "Восстановить пароль')
    def click_reset_password_link(self):
        self.click_element(locators.RESET_PASSWORD_LINK)

    @allure.step('Заполняем поле "Email"')
    def set_email(self, email):
        self.enter_text(locators.EMAIL_FIELD, email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password(self, password):
        self.enter_text(locators.PASSWORD_FIELD, password)

    @allure.step('Кликаем на кнопку "Войти"')
    def click_login_button(self):
        self.click_element(locators.LOGIN_FORM_BUTTON)

    @allure.step('Заполняем логин/пароль и кликаем на кнопку "Войти"')
    def set_email_password_and_login(self, email, password):
        self.open_login_url()
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
