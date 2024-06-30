import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    _ORDER_LIST = [By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]"]
    _ORDER_LIST_ITEM = [By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li"]
    _ORDER_POPUP_HEADER = [By.XPATH, "//section[contains(@class, 'modal_opened')]//p[text()='Cостав']"]
    _ORDER_LIST_ITEM_ID = [By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li//p"]

    def __init__(self, driver):
        super().__init__(driver)

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

    @allure.step('Получаем ID заказа из истории заказов')
    def get_order_id_from_order_history(self):
        return self.get_element_text(self._ORDER_LIST_ITEM_ID)
