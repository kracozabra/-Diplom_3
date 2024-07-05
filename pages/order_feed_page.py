import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import locators


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ждем пока загрузится страница "Лента заказов"')
    def wait_for_load_order_feed_page(self):
        self.wait_for_element_visible(locators.ORDER_FEED_HEADER)

    @allure.step('Ждем пока загрузится список заказов')
    def wait_for_load_order_list(self):
        self.wait_for_element_visible(locators.ORDER_LIST)

    @allure.step('Кликаем на заказ')
    def click_order_list_item(self):
        self.click_element(locators.ORDER_LIST_ITEM)

    @allure.step('Ждем когда откроется попап с заказом')
    def wait_for_order_details_popup(self):
        self.wait_for_element_visible(locators.ORDER_POPUP_HEADER)

    @allure.step('Проверяем, что на попапе с заказом есть заголовок "Состав"')
    def check_order_details_popup_visible(self):
        return self.element_is_present(locators.ORDER_POPUP_HEADER)

    @allure.step('Проверяем, что в списке есть заказ с таким ID')
    def find_order_by_id(self, order_id):
        id_locator = [By.XPATH, locators.ORDER_LIST_ITEM_ID_XPATH.format(order_id)]
        return self.element_is_present(id_locator)

    @allure.step('Получаем количество заказов "За все время"')
    def get_count_orders_all_time(self):
        return self.get_element_text(locators.COUNT_ORDERS_ALL_TIME)

    @allure.step('Получаем количество заказов "За сегодня"')
    def get_count_orders_today(self):
        return self.get_element_text(locators.COUNT_ORDERS_TODAY)

    @allure.step('Получаем id заказа "В работе"')
    def get_order_in_work_id(self):
        return self.get_element_text(locators.ORDER_IN_WORK)

    @allure.step('Ждем пока исчезнет надпись "Все текущие заказы готовы!"')
    def wait_for_order_in_work_appears(self):
        self.wait_for_element_visible(locators.ORDER_IN_WORK_NOW)
