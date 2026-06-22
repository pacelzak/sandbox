from api_frame.auth import Auth 
import pytest 
from helpers.assertions import * 
from helpers.schema import * 
from hypothesis import given
import hypothesis.strategies as st
import allure_pytest



@pytest.mark.parametrize("email, password", [("admin@buzzhive.com", "admin123"), ])
def test_successful_login(auth_api,email, password): 
    
    """Успешная авторизация"""
    response = auth_api.login(email, password) 
    assert_status_code(response, 200) 
    TokenResponse.model_validate(response.json()) 
  
    
    
@pytest.mark.parametrize("email, password", [("frank@buzzhive.com", "frank123")])
def test_banned_login(auth_api,email, password): 
    
    """Авторизация забаненного пользователя"""
    response = auth_api.login(email, password) 
    assert_status_code(response, 400)   


@given(
    email=st.emails(), 
    password=st.text(min_size=8, max_size=20)
)
def test_unsuccessful_login(auth_api, email, password): 
    """Авторизация незарегистрированного пользователя с генерацией случайных данных"""
    
    print(f"\n[Hypothesis Data] Email: {email} | Password: {password}")
    response = auth_api.login(email, password) 
    assert_status_code(response, 401)
    



    
    
