import allure
import config
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_reset_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_url()
        login_page.click_reset_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.wait_for_load_forgot_password_page()
        current_url = forgot_password_page.get_current_url()

        assert current_url == config.FORGOT_PASSWORD_URL

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    def test_set_email_for_reset_password(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_url()
        forgot_password_page.set_email('some@email.ru')
        forgot_password_page.click_forgot_password_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_load_reset_password_page()
        current_url = reset_password_page.get_current_url()

        assert current_url == config.RESET_PASSWORD_URL

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_set_password_field_active(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.open_reset_password_url(driver)
        reset_password_page.click_show_password_password_button()
        reset_password_page.wait_for_password_field_active()

        assert reset_password_page.check_password_field_active()
