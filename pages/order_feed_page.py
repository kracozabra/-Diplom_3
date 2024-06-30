import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    _ORDER_FEED_HEADER = [By.XPATH, "//h1[text()='Лента заказов']"]
    _ORDER_LIST = [By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]"]
    _ORDER_LIST_ITEM = [By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li"]
    _ORDER_POPUP_HEADER = [By.XPATH, "//section[contains(@class, 'modal_opened')]//p[text()='Cостав']"]
    _ORDER_LIST_ITEM_ID_XPATH = "//ul[contains(@class, 'OrderFeed_list')]/li//p[text()='{0}']"
    _COUNT_ORDERS_ALL_TIME = [By.XPATH, "//p[text()='Выполнено за все время:']/../p[2]"]
    _COUNT_ORDERS_TODAY = [By.XPATH, "//p[text()='Выполнено за сегодня:']/../p[2]"]
    _ORDER_IN_WORK = [By.XPATH, "//ul[contains(@class, 'orderListReady')]/li"]
    _NO_ORDERS_IN_WORK = [By.XPATH, "//ul[contains(@class, 'orderListReady')]/li[text()='Все текущие заказы готовы!']"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ждем пока загрузится страница "Лента заказов"')
    def wait_for_load_order_feed_page(self):
        self.wait_for_element_visible(self._ORDER_FEED_HEADER)

    @allure.step('Ждем пока загрузится список заказов')
    def wait_for_load_order_list(self):
        self.wait_for_element_visible(self._ORDER_LIST)

    @allure.step('Кликаем на заказ')
    def click_order_list_item(self):
        self.click_element(self._ORDER_LIST_ITEM)

    @allure.step('Ждем когда откроется попап с заказом')
    def wait_for_order_details_popup(self):
        self.wait_for_element_visible(self._ORDER_POPUP_HEADER)

    @allure.step('Проверяем, что на попапе с заказом есть заголовок "Состав"')
    def check_order_details_popup_visible(self):
        return self.element_is_present(self._ORDER_POPUP_HEADER)

    @allure.step('Проверяем, что в списке есть заказ с таким ID')
    def find_order_by_id(self, order_id):
        id_locator = [By.XPATH, self._ORDER_LIST_ITEM_ID_XPATH.format(order_id)]
        return self.element_is_present(id_locator)

    @allure.step('Получаем количество заказов "За все время"')
    def get_count_orders_all_time(self):
        return self.get_element_text(self._COUNT_ORDERS_ALL_TIME)

    @allure.step('Получаем количество заказов "За сегодня"')
    def get_count_orders_today(self):
        return self.get_element_text(self._COUNT_ORDERS_TODAY)

    @allure.step('Получаем id заказа "В работе"')
    def get_order_in_work_id(self):
        return self.get_element_text(self._ORDER_IN_WORK)

    @allure.step('Ждем пока исчезнет надпись "Все текущие заказы готовы!"')
    def wait_for_order_in_work_appears(self):
        self.wait_for_element_invisible(self._NO_ORDERS_IN_WORK)
