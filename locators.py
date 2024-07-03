from selenium.webdriver.common.by import By

# Локаторы для класса BasePage
PERSONAL_ACCOUNT_LINK = [By.XPATH, "//header//p[text()='Личный Кабинет']"]
CONSTRUCTOR_LINK = [By.XPATH, "//header//p[text()='Конструктор']"]
ORDER_FEED_LINK = [By.XPATH, "//header//p[text()='Лента Заказов']"]

# Локаторы для класса ForgotPasswordPage
FORGOT_PASSWORD_EMAIL_FIELD = [By.XPATH, "//label[text() = 'Email']/../input"]
FORGOT_PASSWORD_HEADER = [By.XPATH, "//h2[text()='Восстановление пароля']"]
FORGOT_PASSWORD_BUTTON = [By.XPATH, "//button[text()='Восстановить']"]

# Локаторы для класса LoginPage
LOGIN_PAGE_HEADER = [By.XPATH, "//h2[text()='Вход']"]
RESET_PASSWORD_LINK = [By.XPATH, "//a[text()='Восстановить пароль']"]
EMAIL_FIELD = [By.XPATH, ".//label[text() = 'Email']/../input"]
PASSWORD_FIELD = [By.XPATH, ".//label[text() = 'Пароль']/../input"]
LOGIN_FORM_BUTTON = [By.XPATH, ".//button[text()='Войти']"]

# Локаторы для класса MainPage
CREATE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
CONSTRUCT_BURGER_HEADER = [By.XPATH, "//h1[text()='Соберите бургер']"]
INGREDIENT_POPUP_HEADER = [By.XPATH, "//h2[text()='Детали ингредиента']"]
INGREDIENT_POPUP_CLOSE_BUTTON = [By.XPATH, "//div[contains(@class, 'Modal')]//button"]
INGREDIENT = [By.XPATH, "//div[contains(@class, 'BurgerIngredients')]//a[1]"]
INGREDIENT_COUNTER2 = [By.XPATH, "//div[contains(@class, 'BurgerIngredients')]//a[1]//div/p[text()=2]"]
BASKET_AREA = [By.XPATH, "//section[contains(@class, 'basket')]"]
ORDER_IN_PROCESS_HEADER = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
ORDER_POPUP_CLOSE_BUTTON = [By.XPATH, "//section[contains(@class, 'modal_opened')]//button"]

# Локаторы для класса ResetPasswordPage
RESET_PASSWORD_HEADER = [By.XPATH, "//h2[text()='Восстановление пароля']"]
RESET_PASSWORD_SAVE_BUTTON = [By.XPATH, "//button[text()='Восстановить']"]
RESET_PASSWORD_ENTER_CODE_FIELD = [By.XPATH, "//label[text() = 'Введите код из письма']/../input"]
RESET_PASSWORD_SHOW_PASSWORD_ICON = [By.XPATH, "//label[text() = 'Пароль']/../div"]
RESET_PASSWORD_PASSWORD_FIELD_ACTIVE = [By.XPATH, "//label[text() = 'Пароль']/../../div[contains(@class, "
                                                  "'input_status_active')]"]

# Локаторы для класса OrderFeedPage
ORDER_FEED_HEADER = [By.XPATH, "//h1[text()='Лента заказов']"]
ORDER_LIST = [By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]"]
ORDER_LIST_ITEM = [By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li"]
ORDER_POPUP_HEADER = [By.XPATH, "//section[contains(@class, 'modal_opened')]//p[text()='Cостав']"]
ORDER_LIST_ITEM_ID_XPATH = "//ul[contains(@class, 'OrderFeed_list')]/li//p[text()='{0}']"
COUNT_ORDERS_ALL_TIME = [By.XPATH, "//p[text()='Выполнено за все время:']/../p[2]"]
COUNT_ORDERS_TODAY = [By.XPATH, "//p[text()='Выполнено за сегодня:']/../p[2]"]
ORDER_IN_WORK = [By.XPATH, "//ul[contains(@class, 'orderListReady')]/li"]
NO_ORDERS_IN_WORK = [By.XPATH, "//ul[contains(@class, 'orderListReady')]/li[text()='Все текущие заказы готовы!']"]

# Локаторы для класса OrderHistoryPage
ORDER_HISTORY_LIST = [By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]"]
ORDER_HISTORY_LIST_ITEM = [By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li"]
ORDER_HISTORY_POPUP_HEADER = [By.XPATH, "//section[contains(@class, 'modal_opened')]//p[text()='Cостав']"]
ORDER_HISTORY_LIST_ITEM_ID = [By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li//p"]

# Локаторы для класса PersonalAccountPage
LOGOUT_LINK = [By.XPATH, ".//button[text()='Выход']"]
ORDER_HISTORY_LINK = [By.XPATH, "//a[text()='История заказов']"]
