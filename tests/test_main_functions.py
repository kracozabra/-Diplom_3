import allure
import config
import helpers
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestMainFunctions:

    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_navigate_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_url()
        login_page.click_constructor_link()
        constructor_page = MainPage(driver)
        constructor_page.wait_for_load_main_page()
        current_url = constructor_page.get_current_url()

        assert current_url == config.MAIN_URL + '/'

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_navigate_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_url()
        main_page.click_order_feed_link()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_load_order_feed_page()
        current_url = order_feed_page.get_current_url()

        assert current_url == config.ORDER_FEED_URL

    @allure.title('Проверка открытия всплывающего окна по клику на игредиент')
    def test_open_ingredient_info(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_url()
        main_page.click_ingredient()
        main_page.wait_for_load_ingredient_popup()

        assert main_page.check_ingredient_popup_header_is_visible()

    @allure.title('Проверка закрытия всплывающего окна по крестику')
    def test_close_ingredient_info(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_url()
        main_page.click_ingredient()
        main_page.wait_for_load_ingredient_popup()
        main_page.click_popup_close_button()
        main_page.wait_for_close_ingredient_popup()

        assert main_page.check_ingredient_popup_header_is_invisible

    @allure.title('Добавление ингредиента в корзину')
    def test_add_ingredient_to_basket(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_url()
        main_page.drag_and_drop_ingredients(driver)

        assert main_page.check_ingredient_counter_equals_2()

    @allure.title('Оформление заказа')
    def test_create_order(self, driver, register_return_login_password_token_delete_user):
        user = register_return_login_password_token_delete_user

        login_page = LoginPage(driver)
        login_page.set_email_password_and_login(user["email"], user["password"])
        login_page.click_constructor_link()
        main_page = MainPage(driver)
        main_page.click_create_order_button()
        main_page.wait_for_order_form()

        assert main_page.check_visibility_order_form
