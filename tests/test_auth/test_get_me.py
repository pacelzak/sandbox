from api_frame.auth import Auth 
from helpers.assertions  import * 
import time

"""def test_get_me_ok(api): 
    

    user : Auth = api(Auth)
    response = user.get_me() 

    assert_status_code(response, 200) 
    assert_message(response, "OK")
    assert_headers(response, "Content-Type", "application/json") 
    assert_response_time(response, 0.25) """


def test_get_me_unreg(auth_api): 
    
    """Незарегистрированный пользователь"""  
    
    response = auth_api.get_me() 
    assert_status_code(response, 403) 
    assert_message(response, "Forbidden")  



def test_failde_get_me(): 
    
    auth = Auth() 
    
    

    
    