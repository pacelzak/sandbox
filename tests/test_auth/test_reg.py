from api_frame.auth import Auth 
import pytest 
from helpers.assertions import * 
import allure_pytest 
from helpers.schema_login import * 
from dotenv import load_dotenv
import os  
load_dotenv() 

moderator_email = os.getenv("moderator")  
moderator_password = os.getenv("moderator_password")  


def test_registration(auth_api, user_data): 

    try:
        """Успешная регистрация нового пользователя"""
        response = auth_api.register(
            user_data['email'],
            user_data['username'],
            user_data['password'],
            user_data['display_name']
        )
        assert_status_code(response, 201) 
        SchemaReg.model_validate(response.json())
    finally:
        requests.post("http://localhost:8000/api/reset")
    

def test_test_registration_with_double_data(auth_api, user_data):  
    
    """регистрация нового пользователя с уже существующим email"""  
    try:
        object = Auth() 
        response = object.register (
            moderator_email,
            user_data['username'],
            user_data['password'],
            user_data['display_name']
        )
        assert_status_code(response, 409) 
    finally: 
        requests.post("http://localhost:8000/api/reset") 
    



    