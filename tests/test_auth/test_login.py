import pytest 
from api_frame.auth import Auth
from helpers.assertions import * 
from helpers.schema_login import * 

import allure_pytest 
from dotenv import load_dotenv
import os  
load_dotenv() 

admin_email = os.getenv("admin")
admin_password = os.getenv("admin_password") 

ban_email = os.getenv("ban_email") 
ban_password = os.getenv("ban_password")



def test_successful_login(auth_api,email, password): 
    
    """Успешная авторизация""" 
    try:
        response = auth_api.login(admin_email, admin_password) 
        assert_status_code(response, 200) 
        SchemaAuth.model_validate(response.json()) 
    finally: 
        requests.post("http://localhost:8000/api/reset")
    
    
@pytest.mark.parametrize("email, password", [(ban_email, ban_password)])
def test_banned_login(auth_api,email, password): 
    
    """Авторизация забаненного пользователя""" 
    try: 
        response = auth_api.login(email, password) 
        assert_status_code(response, 400)   
    finally: 
        requests.post("http://localhost:8000/api/reset")



def test_unsuccessful_login(auth_api, user_data): 
    """Авторизация незарегистрированного пользователя с генерацией случайных данных"""
    
    try:
        response = auth_api.login(user_data["email"], user_data["password"]) 
        assert_status_code(response, 401) 
    finally: 
        requests.post("http://localhost:8000/api/reset") 

def test_login_with_failed_password(auth_api): 
    
    """Авторизация с невереным паролем""" 
    try:
        response = auth_api.login(admin_email, ban_password) 
        assert_status_code(response, 401)
    finally: 
        requests.post("http://localhost:8000/api/reset")


    
    
