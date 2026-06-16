import pytest 
from api_frame.auth import Auth 
from api_frame.base_api import BaseApi
import requests



@pytest.fixture(scope="module")
def auth_api(): 
    
    """Объкт для авторизации/незарегистрированный"""
    return Auth() 



@pytest.fixture(scope="session")
def token():

    def _generate_token(email, password):
        auth = Auth()
        response = auth.login(email, password)
        return response.json()["access_token"]
        
    return _generate_token


@pytest.fixture
def create_session():
   
    def _create(token):
        session = requests.Session()
        # Сразу вшиваем токен в заголовки этой сессии
        session.headers.update({"Authorization": f"Bearer {token}"})
        return session
        
    return _create