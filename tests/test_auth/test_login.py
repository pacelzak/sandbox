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

rebase_url = os.getenv("rebase_url")


def test_successful_login(auth_api): 
    
    """Успешная авторизация""" 
    try:
        response = auth_api.login(admin_email, admin_password) 
        assert_status_code(response, 200) 
        SchemaAuth.model_validate(response.json()) 
    finally: 
        requests.post(rebase_url)
    
    
@pytest.mark.parametrize("email, password", [(ban_email, ban_password)])
def test_banned_login(auth_api,email, password): 
    
    """Авторизация забаненного пользователя""" 
    try: 
        response = auth_api.login(email, password) 
        assert_status_code(response, 400)  
        HTTPErrorDetail.model_validate(response.json()) 
    finally: 
        requests.post(rebase_url)



def test_unsuccessful_login(auth_api, user_data): 
    """Авторизация незарегистрированного пользователя"""
    
    try:
        response = auth_api.login(user_data["email"], user_data["password"]) 
        assert_status_code(response, 401)  
        HTTPErrorDetail.model_validate(response.json())
    finally: 
        requests.post(rebase_url) 

def test_login_with_failed_password(auth_api): 
    
    """Авторизация зарегистрированного пользователя с невереным паролем""" 
    try:
        response = auth_api.login(admin_email, ban_password) 
        assert_status_code(response, 401)
        HTTPErrorDetail.model_validate(response.json())
    finally: 
        requests.post(rebase_url)


@pytest.mark.parametrize(
    "email, password, expected_status",
    [(admin_email, "", 401), ("", admin_password, 422), ("", "", 422)],
)
def test_login_with_empty_field(auth_api, email, password, expected_status):
    """Авторизация c пустыми полями"""
    try:
        response = auth_api.login(email, password)
        assert_status_code(response, expected_status)

        # Выбираем схему в зависимости от статуса ответа
        if expected_status == 422:
            HTTPValidationError.model_validate(response.json())
        else:
            # Для 401 (и возможно 400/403, если там тоже строки)
            HTTPErrorDetail.model_validate(response.json())

    finally:
        requests.post(rebase_url)
    





    
    
