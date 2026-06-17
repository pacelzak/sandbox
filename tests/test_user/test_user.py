from api_frame.users import Users 
from api_frame.auth import Auth  
from helpers.assertions import * 
import allure_pytest

def test_list_users(api, token):
    get_token = token("admin@buzzhive.com", "admin123")
    user_client: Users = api(Users, get_token) 
    try:
        response = user_client.list_users() 
        assert_status_code(response, 200) 
        assert_message(response, "OK")  
    finally:
        requests.post("http://localhost:8000/api/reset")

def test_apdate_me(api, token): 
    get_token = token("admin@buzzhive.com", "admin123")
    user_client: Users = api(Users, get_token) 
    
    try:
        display_name = "pav"
        bio = "secondfersion"
        is_private = True
        
        response = user_client.update_me(display_name, bio, is_private) 
        assert response.json()['display_name'] == display_name  
    finally:
        requests.post("http://localhost:8000/api/reset")
    

def test_get_user_posts(api, token):  
    get_token = token("admin@buzzhive.com", "admin123") 
    user: Users = api(Users, get_token)  
    try:
        list_user_name = user.list_users() 
        user_name = list_user_name.json()["items"][1]["username"]
        user_post = user.get_user_post(user_name) 
        assert_status_code(user_post, 200) 
    finally:
        requests.post("http://localhost:8000/api/reset")