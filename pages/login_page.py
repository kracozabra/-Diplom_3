import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    _LOGIN_PAGE_HEADER = [By.XPATH, "//h2[text()='Вход']"]
    _RESET_PASSWORD_LINK = [By.XPATH, "//a[text()='Восстановить пароль']"]
    _EMAIL_FIELD = [By.XPATH, ".//label[text() = 'Email']/../input"]
    _PASSWORD_FIELD = [By.XPATH, ".//label[text() = 'Пароль']/../input"]
    _LOGIN_FORM_BUTTON = [By.XPATH, ".//button[text()='Войти']"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку страницы логина')
    def wait_for_load_login_page(self):
        self.wait_for_element_visible(self._LOGIN_PAGE_HEADER)

    @allure.step('Кликаем на кнопку "Восстановить пароль')
    def click_reset_password_link(self):
        self.click_element(self._RESET_PASSWORD_LINK)

    @allure.step('Заполняем поле "Email"')
    def set_email(self, email):
        self.enter_text(self._EMAIL_FIELD, email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password(self, password):
        self.enter_text(self._PASSWORD_FIELD, password)

    @allure.step('Кликаем на кнопку "Войти"')
    def click_login_button(self):
        self.click_element(self._LOGIN_FORM_BUTTON)

    @allure.step('Заполняем логин/пароль и кликаем на кнопку "Войти"')
    def set_email_password_and_login(self, email, password):
        self.open_login_url()
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
