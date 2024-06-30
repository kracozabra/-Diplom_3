import allure
import config
import helpers
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода на страницу персонального профиля')
    def test_navigate_to_personal_account(self, driver):
        user = helpers.register_new_user_and_return_login_password_token()

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_personal_account_link()
        personal_account_page.wait_for_load_personal_account_page()
        current_url = personal_account_page.get_current_url()

        assert current_url == config.PERSONAL_ACCOUNT_URL

        helpers.delete_user_by_token(user["token"])

    @allure.title('Переход в раздел "История заказов"')
    def test_navigate_to_order_history(self, driver):
        user = helpers.register_new_user_and_return_login_password_token()

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_personal_account_link()
        personal_account_page.wait_for_load_personal_account_page()
        personal_account_page.click_order_history_link()
        current_url = personal_account_page.get_current_url()

        assert current_url == config.ORDER_HISTORY_URL

        helpers.delete_user_by_token(user["token"])

    @allure.title('Выход из аккаунта')
    def test_exit_from_account(self, driver):
        user = helpers.register_new_user_and_return_login_password_token()

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_personal_account_link()
        personal_account_page.wait_for_load_personal_account_page()
        personal_account_page.click_logout_link()
        login_page.wait_for_load_login_page()
        current_url = personal_account_page.get_current_url()

        assert current_url == config.LOGIN_URL

        helpers.delete_user_by_token(user["token"])
