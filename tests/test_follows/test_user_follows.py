from api_frame.follows import Follows 
from api_frame.users import Users 
from helpers.assertions import *  
import requests
import allure_pytest  

from dotenv import load_dotenv
import os  
load_dotenv() 

moderator_email = os.getenv("moderator")  
moderator_password = os.getenv("moderator_password")  

admin_email = os.getenv("admin")  
admin_password = os.getenv("admin_password")  


ban_email = os.getenv("ban_email") 
ban_password = os.getenv("ban_password")  

dav_email = os.getenv("dav_email") 
dav_password = os.getenv("dav_password") 

def test_follows_on_private(create_session, token):

    """Подписка на приватный канал"""

    admin_token = token(admin_email, admin_password) 
    mod_token = token(moderator_email, moderator_password) 
    admin_session = create_session(admin_token)
    mod_session = create_session(mod_token)
    user_admin = Users(session=admin_session)
    follow_user = Follows(session=admin_session)
    follow_mod = Follows(session=mod_session)

    try:       

        user_admin.update_me(is_private=True)  
        requests_follow = follow_mod.follow_user("admin") 
        id_requests = requests_follow.json()["id"] 
        accept_requests = follow_user.accept_follow_requests(id_requests) 
        assert_status_code(accept_requests, 200)
        
    finally: 
        requests.post("http://localhost:8000/api/reset") 

def test_follows(create_session, token): 
    
    """Подписка не на приватный аккаунт""" 
    
    admin_token = token(admin_email, admin_password) 
    mod_token = token(moderator_email, moderator_password) 
    admin_session = create_session(admin_token)
    mod_session = create_session(mod_token)
    follow_mod = Follows(session=mod_session)
    user_mod = Users(session=mod_session)

    try:       

        requests_follow = follow_mod.follow_user("admin") 
        list_following = user_mod.get_following("moderator").json()   
        list_user = [i["username"] for i in list_following["items"]] 
        assert "admin" in list_user
        
        
    finally: 
        requests.post("http://localhost:8000/api/reset") 

def test_follows_on_banned_user(create_session, token): 
    
    """Подписка на забаненного пользователя""" 
    
    admin_session = create_session(token(admin_email, admin_password)) 
    admin_follows = Follows(admin_session)
    
    try: 
        method_follows = admin_follows.follow_user("frank_banned") 
        assert_status_code(method_follows, 201)
    finally: 
        requests.post("http://localhost:8000/api/reset") 

def test_unfollow_user(create_session, token): 
    
    """Отписка от пользователя""" 
    
    admin_session = create_session(token(admin_email, admin_password)) 
    mod_session = create_session(token(moderator_email, moderator_password)) 
    follow_user = Follows(session=admin_session)
    follow_mod = Follows(session=mod_session) 
    
    try: 
        requests_follows = follow_mod.follow_user("admin")  
        unfollow = follow_mod.unfollow_user("admin") 
        assert_status_code(unfollow, 204)
    finally: 
        requests.post("http://localhost:8000/api/reset") 


def test_reject_follow(create_session, token): 
    
    """Отклонение подписки на приватный аккаунт"""
    
    admin_token = token(admin_email, admin_password) 
    mod_token = token(moderator_email, moderator_password) 
    admin_session = create_session(admin_token)
    mod_session = create_session(mod_token)
    user_admin = Users(session=admin_session)
    follow_admin = Follows(session=admin_session)
    follow_mod = Follows(session=mod_session)

    try:       

        user_admin.update_me(is_private=True)  
        requests_follow = follow_mod.follow_user("admin") 
        id_requests = requests_follow.json()["id"] 
        reject = follow_admin.reject_follow_requests(id_requests) 
        assert_status_code(reject, 204)
    
    finally:
        requests.post("http://localhost:8000/api/reset") 
        
        
def test_list_requests(create_session, token): 
    
    """Список запросов"""
    
    admin_token = token(admin_email, admin_password) 
    admin_session = create_session(admin_token)
    user_admin = Users(session=admin_session)
    follow_admin = Follows(session=admin_session) 
    
    mod_token = token(moderator_email, moderator_password)  
    mod_session = create_session(mod_token)
    follow_mod = Follows(session=mod_session)
    
    mod_token2 = token(dav_email, dav_password)  
    mod_session2 = create_session(mod_token2)
    follow_mod2 = Follows(session=mod_session2)

    try:       

        user_admin.update_me(is_private=True)  
        list_id = follow_mod.follow_user("admin").json() 
        id_requests = list_id["id"]
        list_id2 = follow_mod2.follow_user("admin").json() 
        res = follow_admin.get_follow_requests().json() 
        list_id = [i["id"] for i in res["items"]]
        assert id_requests in list_id
    
    finally:
        requests.post("http://localhost:8000/api/reset")
    
    
   
    
    
    
    
    
    
    
    
   
