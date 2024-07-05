import json
import allure
import requests
from faker import Faker

# URL-ы и ENDPOINT-ы
URL = 'https://stellarburgers.nomoreparties.site'
REGISTER_USER_ENDPOINT = URL + '/api/auth/register'
GET_CHANGE_USER_INFO = URL + '/api/auth/user'
CREATE_ORDER_ENDPOINT = URL + '/api/orders'
GET_INGREDIENTS = URL + '/api/ingredients'

# Дополнительная информация для запросов
headers_json = {"Content-type": "application/json"}


@allure.step('Генерируем случайные данные для создания пользователя')
def generate_random_user_data():
    fake = Faker(locale="ru_Ru")

    user_create_data = {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name()
    }
    return user_create_data


@allure.step('Создаем нового пользователя и возвращаем его логин, пароль и токен')
def register_new_user_and_return_login_password_token():
    payload = generate_random_user_data()
    user_login_data = {}
    response = requests.post(REGISTER_USER_ENDPOINT, data=payload)
    if response.status_code == 200:
        user_login_data = {
            "email": payload['email'],
            "password": payload['password'],
            "token": response.json()['accessToken']
        }
    return user_login_data


@allure.step('Удаляем пользователя по его токену')
def delete_user_by_token(token):
    response = requests.delete(GET_CHANGE_USER_INFO, headers={'Authorization': token})


@allure.step('Создаем список существующих ингредиентов')
def get_random_ingredients(number):
    ingredients = []
    response = requests.get(GET_INGREDIENTS)
    for i in range(number):
        ingredients.append(response.json()['data'][i]['_id'])
    return ingredients


@allure.step('Создаем заказ по токену и возвращаем его id')
def create_order(token):
    payload = {"ingredients": get_random_ingredients(5)}
    payload_json = json.dumps(payload)
    response = requests.post(CREATE_ORDER_ENDPOINT, data=payload_json,
                             headers={'Authorization': token, "Content-type": "application/json"})
    return response.json()["order"]["number"]
