from api_frame.auth import Auth 
import pytest 
from helpers.data_generator import Genetator 
from helpers.assertions import * 

fake = Genetator() 

test_users = [
    (fake.email, fake.username, fake.password, fake.display_name),
    (fake.email, fake.username, fake.password, fake.display_name),
    (fake.email, fake.username, fake.password, fake.display_name),
]

@pytest.mark.parametrize("email, username, password, display_name", test_users)
def test_registration(auth_api, email, username, password, display_name): 

    """Успешная регистрация нового пользователя"""
    response = auth_api.register(email, username, password, display_name)
    assert_status_code(response, 201) 




    