from api_frame.auth import Auth 
from helpers.assertions  import * 
import time 
import allure_pytest

def test_get_me_ok(token,create_session): 
    
    """Информация о пользователе"""
    get_token = token("admin@buzzhive.com", "admin123") 
    admin_session = create_session(get_token)
    user_client = Auth(session=admin_session) 
    response = user_client.get_me() 
    assert_status_code(response, 200) 
    assert_message(response, "OK")
    assert_headers(response, "Content-Type", "application/json") 
    assert_response_time(response, 0.25) 


def test_get_me_unreg(auth_api): 
    
    """Незарегистрированный пользователь"""  
    
    response = auth_api.get_me() 
    assert_status_code(response, 403) 
    assert_message(response, "Forbidden")  



    
    

    
    