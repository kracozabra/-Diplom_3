import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    _FORGOT_PASSWORD_EMAIL_FIELD = [By.XPATH, "//label[text() = 'Email']/../input"]
    _FORGOT_PASSWORD_HEADER = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    _FORGOT_PASSWORD_BUTTON = [By.XPATH, "//button[text()='Восстановить']"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку страницы "Восстановить пароль"')
    def wait_for_load_forgot_password_page(self):
        self.wait_for_element_visible(self._FORGOT_PASSWORD_HEADER)

    @allure.step('Заполняем Email на форме восстановления пароля')
    def set_email(self, email):
        self.enter_text(self._FORGOT_PASSWORD_EMAIL_FIELD, email)

    @allure.step('Кликаем на кнопку "Восстановить пароль')
    def click_forgot_password_button(self):
        self.click_element(self._FORGOT_PASSWORD_BUTTON)
