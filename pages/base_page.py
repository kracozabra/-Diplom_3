import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
import config
import locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден спустя {timeout} секунд')
            return None

    def get_element_text(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            return element.text
        else:
            print(f'Не получилось получить текст жлемента с локатором {locator}')
            return None

    def scroll_to_element(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        else:
            print(f'Не получилось проскроллить до элемента с локатором {locator}')
            return None

    def click_element(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f'Не получилось кликнуть по элементу с локатором {locator}')

    def enter_text(self, locator, text, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Ошибка при попытке ввода текста в элемент с локатором {locator}')

    def wait_for_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден спустя {timeout} секунд')
            return None

    def wait_for_element_invisible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} найден спустя {timeout} секунд')
            return None

    def wait_for_title(self, title, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.title_contains(title))
        except TimeoutException:
            print(f'Страница с title "{title}" не открылась спустя {timeout} секунд')
            return None

    def element_is_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден спустя {timeout} секунд')
            return None

    def element_is_clickable(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            print(f'Элемент с локатором {locator} не доступен спустя {timeout} секунд')
            return None

    def element_is_not_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            print(f'Элемент с локатором {locator} найден спустя {timeout} секунд')
            return None

    def drag_drop_elements(self, driver, locator1, locator2):
        source = self.find_element(locator1)
        target = self.find_element(locator2)
        drag_and_drop(driver, source, target)

    def refresh_page(self):
        self.driver.refresh()

    @allure.step('Открываем главную страницу')
    def open_main_url(self):
        self.navigate(config.MAIN_URL)

    @allure.step('Открываем страницу логина')
    def open_login_url(self):
        self.navigate(config.LOGIN_URL)

    @allure.step('Открываем страницу напоминания пароля')
    def open_forgot_password_url(self):
        self.navigate(config.FORGOT_PASSWORD_URL)

    @allure.step('Открываем страницу личного профиля')
    def open_personal_account_url(self):
        self.navigate(config.PERSONAL_ACCOUNT_URL)

    @allure.step('Открываем страницу "Лента заказов"')
    def open_order_feed_url(self):
        self.navigate(config.ORDER_FEED_URL)

    @allure.step('Открываем страницу "История заказов"')
    def open_order_history_url(self):
        self.navigate(config.ORDER_HISTORY_URL)

    @allure.step('Получаем URL текущей вкладки')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Кликаем по ссылке личного профиля')
    def click_personal_account_link(self):
        self.click_element(locators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Кликаем по ссылке "Конструктор"')
    def click_constructor_link(self):
        self.click_element(locators.CONSTRUCTOR_LINK)

    @allure.step('Кликаем по ссылке "Лента заказов"')
    def click_order_feed_link(self):
        self.click_element(locators.ORDER_FEED_LINK)
