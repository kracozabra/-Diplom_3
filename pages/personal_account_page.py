import allure
from pages.base_page import BasePage
import locators


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку страницы личного профиля')
    def wait_for_load_personal_account_page(self):
        self.wait_for_element_visible(locators.LOGOUT_LINK)

    @allure.step('Нажимаем на ссылку "История заказов"')
    def click_order_history_link(self):
        self.click_element(locators.ORDER_HISTORY_LINK)

    @allure.step('Нажимаем на ссылку "Выход"')
    def click_logout_link(self):
        self.click_element(locators.LOGOUT_LINK)
