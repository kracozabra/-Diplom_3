import allure
from pages.base_page import BasePage
import locators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ждем пока загрузится кнопка "Оформить заказ"')
    def wait_for_load_create_order_button(self):
        self.wait_for_load_create_order_button(locators.CREATE_ORDER_BUTTON)

    @allure.step('Ждем пока загрузится главная страница')
    def wait_for_load_main_page(self):
        self.wait_for_element_visible(locators.CONSTRUCT_BURGER_HEADER)

    @allure.step('Кликаем на ингредиент в конструкторе')
    def click_ingredient(self):
        self.click_element(locators.INGREDIENT)

    @allure.step('Ждем пока загрузится попап с инфо об инредиенте')
    def wait_for_load_ingredient_popup(self):
        self.wait_for_element_visible(locators.INGREDIENT_POPUP_HEADER)

    @allure.step('Проверяем видимость заголовка попапа с инфо об ингредиенте')
    def check_ingredient_popup_header_is_visible(self):
        return self.element_is_present(locators.INGREDIENT_POPUP_HEADER)

    @allure.step('Проверяем НЕвидимость заголовка попапа с инфо об ингредиенте')
    def check_ingredient_popup_header_is_invisible(self):
        return self.element_is_not_present(locators.INGREDIENT_POPUP_HEADER)

    @allure.step('Ждем пока закроется попап с инфо об инредиенте')
    def wait_for_close_ingredient_popup(self):
        self.wait_for_element_invisible(locators.INGREDIENT_POPUP_HEADER)

    @allure.step('Кликаем на крестик для закрытия попапа')
    def click_popup_close_button(self):
        self.click_element(locators.INGREDIENT_POPUP_CLOSE_BUTTON)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_create_order_button(self):
        self.click_element(locators.CREATE_ORDER_BUTTON)

    @allure.step('Кладем ингредиент в корзину"')
    def drag_and_drop_ingredients(self, driver):
        self.drag_drop_elements(driver, locators.INGREDIENT, locators.BASKET_AREA)

    @allure.step('Провереряем, что на счетчике ингредиента стоит значение "2"')
    def check_ingredient_counter_equals_2(self):
        return self.element_is_present(locators.INGREDIENT_COUNTER2)

    @allure.step('Ждем когда появится окно оформленного заказа')
    def wait_for_order_form(self):
        self.wait_for_element_visible(locators.ORDER_IN_PROCESS_HEADER)

    @allure.step('Проверяем видимость заголовка попапа с инфо об ингредиенте')
    def check_visibility_order_form(self):
        return self.element_is_present(locators.ORDER_IN_PROCESS_HEADER)

    @allure.step('Закрываем окно попапа')
    def click_close_popup_button(self):
        self.click_element(locators.ORDER_POPUP_CLOSE_BUTTON)

    @allure.step('Ждем пока кнопка закрытия попапа станет доступна')
    def wait_for_close_popup_button_is_clickable(self):
        self.element_is_clickable(locators.ORDER_POPUP_CLOSE_BUTTON)
