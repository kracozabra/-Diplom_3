import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    _LOGOUT_LINK = [By.XPATH, ".//button[text()='Выход']"]
    _ORDER_HISTORY_LINK = [By.XPATH, "//a[text()='История заказов']"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку страницы личного профиля')
    def wait_for_load_personal_account_page(self):
        self.wait_for_element_visible(self._LOGOUT_LINK)

    @allure.step('Нажимаем на ссылку "История заказов"')
    def click_order_history_link(self):
        self.click_element(self._ORDER_HISTORY_LINK)

    @allure.step('Нажимаем на ссылку "Выход"')
    def click_logout_link(self):
        self.click_element(self._LOGOUT_LINK)
