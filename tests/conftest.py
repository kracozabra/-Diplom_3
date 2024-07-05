import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

import helpers
from helpers import generate_random_user_data


# Помогает корректно выводить символы кириллицы в консоли PyCharm
def pytest_make_parametrize_id(config, val):
    return repr(val)


def _get_driver(name):
    if name == 'chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == 'firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise TypeError('Driver is not found')


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = _get_driver(request.param)
    yield driver
    driver.quit()


@pytest.fixture
def register_return_login_password_token_delete_user():
    user = helpers.register_new_user_and_return_login_password_token()
    yield user
    helpers.delete_user_by_token(user["token"])
