from api_frame.auth import Auth 
import pytest 
from helpers.assertions import * 
import allure_pytest 


def test_registration(auth_api, user_data): 

    """Успешная регистрация нового пользователя"""
    response = auth_api.register(
        user_data['email'],
        user_data['username'],
        user_data['password'],
        user_data['display_name']
    )
    assert_status_code(response, 201) 




    