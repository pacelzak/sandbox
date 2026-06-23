from api_frame.users import Users 
from api_frame.auth import Auth  
from helpers.assertions import * 
import allure_pytest
from helpers.schema_login import * 

from dotenv import load_dotenv
import os  
load_dotenv() 


admin_email = os.getenv("admin")  
admin_password = os.getenv("admin_password")  

rebase_url = os.getenv("rebase_url")

def test_list_users(create_session, token):
    get_token = token(admin_email, admin_password) 
    admin_session = create_session(get_token)
    user_client = Users(session=admin_session)
    try:
        response = user_client.list_users() 
        assert_status_code(response, 200) 
        assert_message(response, "OK")   
        UserPaginatedResponse.model_validate(response.json())
    finally:
        requests.post(rebase_url)

def test_apdate_me(create_session, token): 
    get_token = token(admin_email, admin_password) 
    admin_session = create_session(get_token)
    user_client = Users(session=admin_session)
    
    try:
        display_name = "pav"
        bio = "secondfersion"
        is_private = True
        
        response = user_client.update_me(display_name, bio, is_private) 
        assert response.json()['display_name'] == display_name  
    finally:
        requests.post(rebase_url)
    

def test_get_user_posts(create_session, token):  
    get_token = token(admin_email, admin_password) 
    admin_session = create_session(get_token)
    user_client = Users(session=admin_session)
    try:
        list_user_name = user_client.list_users() 
        user_name = list_user_name.json()["items"][1]["username"]
        user_post = user_client.get_user_post(user_name) 
        assert_status_code(user_post, 200) 
    finally:
        requests.post(rebase_url)