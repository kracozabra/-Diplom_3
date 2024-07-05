import allure
import helpers
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:

    @allure.title('Проверка открытия всплывающего окна после клика на заказ')
    def test_click_on_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_url()
        order_feed_page.wait_for_load_order_list()
        order_feed_page.click_order_list_item()
        order_feed_page.wait_for_order_details_popup()

        assert order_feed_page.check_order_details_popup_visible()

    @allure.title('Проверка что заказы  из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_from_history_displayed_on_order_feed(self, driver, register_return_login_password_token_delete_user):
        user = register_return_login_password_token_delete_user
        helpers.create_order(user["token"])

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        login_page.click_personal_account_link()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_order_history_link()
        order_history_page = OrderHistoryPage(driver)
        order_history_page.wait_for_load_order_list()
        order_id = order_history_page.get_order_id_from_order_history()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_order_feed_link()
        order_feed_page.wait_for_load_order_list()

        assert order_feed_page.find_order_by_id(order_id)

    @allure.title('Проверка что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_increase_counter_orders_all_time(self, driver, register_return_login_password_token_delete_user):
        user = register_return_login_password_token_delete_user

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_load_order_feed_page()
        order_feed_page.click_order_feed_link()
        order_feed_page.wait_for_load_order_list()
        counter_before = int(order_feed_page.get_count_orders_all_time())
        helpers.create_order(user["token"])
        order_feed_page.refresh_page()
        order_feed_page.wait_for_load_order_list()
        counter_after = int(order_feed_page.get_count_orders_all_time())

        assert counter_before < counter_after

    @allure.title('Проверка что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_increase_counter_orders_today(self, driver, register_return_login_password_token_delete_user):
        user = register_return_login_password_token_delete_user

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_load_order_feed_page()
        order_feed_page.click_order_feed_link()
        order_feed_page.wait_for_load_order_list()
        counter_before = int(order_feed_page.get_count_orders_today())
        helpers.create_order(user["token"])
        order_feed_page.refresh_page()
        order_feed_page.wait_for_load_order_list()
        counter_after = int(order_feed_page.get_count_orders_today())

        assert counter_before < counter_after

    @allure.title('Проверка что после оформления заказа его номер появляется в разделе "В работе"')
    def test_order_is_displayed_in_work(self, driver, register_return_login_password_token_delete_user):
        user = register_return_login_password_token_delete_user

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_order_feed_link()
        order_feed_page.wait_for_load_order_list()
        order_id = '0' + str(helpers.create_order(user["token"]))
        order_feed_page.wait_for_order_in_work_appears()
        order_in_work_id = order_feed_page.get_order_in_work_id()

        assert order_in_work_id == order_id
