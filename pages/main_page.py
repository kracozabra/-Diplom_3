import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    _CREATE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    _CONSTRUCT_BURGER_HEADER = [By.XPATH, "//h1[text()='Соберите бургер']"]
    _INGREDIENT_POPUP_HEADER = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    _INGREDIENT_POPUP_CLOSE_BUTTON = [By.XPATH, "//div[contains(@class, 'Modal')]//button"]
    _INGREDIENT = [By.XPATH, "//div[contains(@class, 'BurgerIngredients')]//a[1]"]
    _INGREDIENT_COUNTER2 = [By.XPATH, "//div[contains(@class, 'BurgerIngredients')]//a[1]//div/p[text()=2]"]
    _BASKET_AREA = [By.XPATH, "//section[contains(@class, 'basket')]"]
    _ORDER_IN_PROCESS_HEADER = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
    _ORDER_POPUP_CLOSE_BUTTON = [By.XPATH, "//section[contains(@class, 'modal_opened')]//button"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ждем пока загрузится кнопка "Оформить заказ"')
    def wait_for_load_create_order_button(self):
        self.wait_for_load_create_order_button(self._CREATE_ORDER_BUTTON)

    @allure.step('Ждем пока загрузится главная страница')
    def wait_for_load_main_page(self):
        self.wait_for_element_visible(self._CONSTRUCT_BURGER_HEADER)

    @allure.step('Кликаем на ингредиент в конструкторе')
    def click_ingredient(self):
        self.click_element(self._INGREDIENT)

    @allure.step('Ждем пока загрузится попап с инфо об инредиенте')
    def wait_for_load_ingredient_popup(self):
        self.wait_for_element_visible(self._INGREDIENT_POPUP_HEADER)

    @allure.step('Проверяем видимость заголовка попапа с инфо об ингредиенте')
    def check_ingredient_popup_header_is_visible(self):
        return self.element_is_present(self._INGREDIENT_POPUP_HEADER)

    @allure.step('Проверяем НЕвидимость заголовка попапа с инфо об ингредиенте')
    def check_ingredient_popup_header_is_invisible(self):
        return self.element_is_not_present(self._INGREDIENT_POPUP_HEADER)

    @allure.step('Ждем пока закроется попап с инфо об инредиенте')
    def wait_for_close_ingredient_popup(self):
        self.wait_for_element_invisible(self._INGREDIENT_POPUP_HEADER)

    @allure.step('Кликаем на крестик для закрытия попапа')
    def click_popup_close_button(self):
        self.click_element(self._INGREDIENT_POPUP_CLOSE_BUTTON)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_create_order_button(self):
        self.click_element(self._CREATE_ORDER_BUTTON)

    @allure.step('Кладем ингредиент в корзину"')
    def drag_and_drop_ingredients(self, driver):
        self.drag_drop_elements(driver, self._INGREDIENT, self._BASKET_AREA)

    @allure.step('Провереряем, что на счетчике ингредиента стоит знаечние "2"')
    def check_ingredient_counter_equals_2(self):
        return self.element_is_present(self._INGREDIENT_COUNTER2)

    @allure.step('Ждем когда появится окно оформленного заказа')
    def wait_for_order_form(self):
        self.wait_for_element_visible(self._ORDER_IN_PROCESS_HEADER)

    @allure.step('Проверяем видимость заголовка попапа с инфо об ингредиенте')
    def check_visibility_order_form(self):
        return self.element_is_present(self._ORDER_IN_PROCESS_HEADER)

    @allure.step('Закрываем окно попапа')
    def click_close_popup_button(self):
        self.click_element(self._ORDER_POPUP_CLOSE_BUTTON)

    @allure.step('Ждем пока кнопка закрытия попапа станет доступна')
    def wait_for_close_popup_button_is_clickable(self):
        self.element_is_clickable(self._ORDER_POPUP_CLOSE_BUTTON)
