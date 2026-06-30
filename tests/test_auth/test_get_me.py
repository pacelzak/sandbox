from api_frame.auth import Auth 
from helpers.assertions  import *  
from helpers.schema_login  import *  
import allure_pytest
from dotenv import load_dotenv
import os  
load_dotenv() 

admin_email = os.getenv("admin")
admin_password = os.getenv("admin_password")

rebase_url = os.getenv("rebase_url")


def test_get_me_ok(token,create_session): 
    
    """Информация о пользователе""" 
    try:
        get_token = token(admin_email, admin_password) 
        admin_session = create_session(get_token)
        user_client = Auth(session=admin_session) 
        response = user_client.get_me() 
        assert_status_code(response, 200) 
        assert_message(response, "OK")
        assert_headers(response, "Content-Type", "application/json") 
        SchemaReg.model_validate(response.json())
    finally: 
        requests.post(rebase_url)


def test_get_me_unreg(auth_api): 
    
    """Незарегистрированный пользователь"""  
    
    try:
        response = auth_api.get_me() 
        assert_status_code(response, 403) 
        assert_message(response, "Forbidden")  
        HTTPErrorDetail.model_validate(response.json())
    finally: 
        requests.post(rebase_url)


    
    

    
    