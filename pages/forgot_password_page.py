import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import locators


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку страницы "Восстановить пароль"')
    def wait_for_load_forgot_password_page(self):
        self.wait_for_element_visible(locators.FORGOT_PASSWORD_HEADER)

    @allure.step('Заполняем Email на форме восстановления пароля')
    def set_email(self, email):
        self.enter_text(locators.FORGOT_PASSWORD_EMAIL_FIELD, email)

    @allure.step('Кликаем на кнопку "Восстановить пароль')
    def click_forgot_password_button(self):
        self.click_element(locators.FORGOT_PASSWORD_BUTTON)
