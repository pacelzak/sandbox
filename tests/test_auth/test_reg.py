from api_frame.auth import Auth 
from helpers.assertions import * 
import allure
from helpers.schema_login import * 
from dotenv import load_dotenv
import os  
load_dotenv() 

moderator_email = os.getenv("moderator")  
moderator_password = os.getenv("moderator_password")   


rebase_url = os.getenv("rebase_url")

@allure.severity("high")
def test_registration(auth_api, user_data): 

    try:
        """Успешная регистрация нового пользователя"""
        response = auth_api.register(
            user_data['email'],
            user_data['username'],
            user_data['password'],
            user_data['display_name']
        )
        assert_status_code(response, 201)  
        SchemaReg.model_validate(response.json()) 
        assert_json_value(response, "email", user_data['email']) 
        assert_json_value(response, "username", user_data['username'])  
        assert_json_value(response, "display_name", user_data['display_name'])  
        assert_message(response, "Created")
        assert_headers(response, "content-type","application/json")
    finally:
        requests.post(rebase_url)
    
@pytest.mark.parametrize("duplicate_type, expected_status", [
    ("email", 409),        # Дублируем email
    ("username", 409),     # Дублируем username
])
def test_registration_with_double_data(auth_api, duplicate_type, expected_status, user_data):  
    
    """регистрация нового пользователя с уже существующим данными"""  
    try:
        email = user_data['email'] 
        username= user_data['username'] 
        if duplicate_type=='email': 
            email = moderator_email 
        if duplicate_type=='username': 
            email = moderator_email 
        response = auth_api.register (
            email,
            username, 
            user_data['password'],
            user_data["display_name"] 
        )
        assert_status_code(response, expected_status) 
    finally: 
        requests.post(rebase_url) 


        
@pytest.mark.parametrize("email, username, password, display_name, expected_status", [
    ("", "valid_user", "ValidPass123", "Name", 422),              
    ("user@test.com", "", "ValidPass123", "Name", 422),    
    ("user@test.com", "valid_user", "", "Name", 422),             
    ("user@test.com", "valid_user", "ValidPass123", "", 422),         
])   
def test_registration_with_empty_field(auth_api, email, username, password, display_name, expected_status): 
    
    """"Регистрация с пустыми полями""" 
    
    try:
        response = auth_api.register (
            email,
            username,
            password,
            display_name
        )
        assert_status_code(response, expected_status) 
    finally: 
        requests.post(rebase_url)     



@pytest.mark.parametrize("username, expected_status", [
    ("aa", 422),                 # Сервер вернул 422 (валидация min_length: 3 сработала)
    ("aaa", 201),                # Успешно (3 символа)
    ("a" * 30, 201),            # Успешно
    ("a" * 31, 422),            # Сервер вернул 422 (валидация max_length: 31 сработала) max_length
])
@allure.severity("normal")
def test_username_field(auth_api, username, expected_status):
    """Тестирование граничных значений для длины username"""
    try:
        unique_email = f"test_{username[:10]}_{len(username)}@example.com"
        response = auth_api.register(
            unique_email,
            username=username,
            password="ValidPassword123",
            display_name="Test Name"
        )
        
        assert_status_code(response, expected_status)
    finally: 
        requests.post(rebase_url)  


@pytest.mark.parametrize("password, expected_status", [
    ("a" * 5, 422),                 # Сервер вернул 422 (валидация min_length: 3 сработала)
    ("a" * 6, 201),                # Успешно (3 символа)
    ("a" * 128, 201),            # Успешно
    ("a" * 129, 422),            # Сервер вернул 422 (валидация max_length: 129 сработала) max_length
])
@allure.severity("normal")
def test_password_field(auth_api, user_data, password, expected_status):
    """Тестирование граничных значений для длины password"""
    try:
        response = auth_api.register(
            user_data["email"],
            user_data["username"],
            password,
            display_name="Test Name"
        )
        
        assert_status_code(response, expected_status)
    finally: 
        requests.post(rebase_url)  

@pytest.mark.parametrize("display_name, expected_status", [
    ("a" , 201),                 # Сервер вернул 422 (валидация min_length: 3 сработала)
    ('', 422),                # Успешно (3 символа)
    ("a" * 100, 201),            # Успешно
    ("a" * 101, 422),            # Сервер вернул 422 (валидация max_length: 129 сработала) max_length
])
@allure.severity("normal")
def test_display_name_field(auth_api, user_data, display_name, expected_status):
    """Тестирование граничных значений для длины display_name"""
    try:
        response = auth_api.register(
            user_data["email"],
            user_data["username"],
            user_data["password"],
            display_name
        )
        
        assert_status_code(response, expected_status)
    finally: 
        requests.post(rebase_url)  


@pytest.mark.parametrize("email, expected_status", [
    ("example" , 422),                
    ('example@mail', 422),                
    ("examplemail.com", 422),          
    ("example@@email.com", 422), 
    ("user.name@mail.com", 201),
    ("user_name@mail.com", 201) 
             
])
@allure.severity("normal")
def test_display_name_field(auth_api, user_data, email, expected_status):
    """Тестирование граничных значений для длины display_name"""
    try:
        response = auth_api.register(
            email,
            user_data["username"],
            user_data["password"],
            user_data["display_name"]
        )
        
        assert_status_code(response, expected_status)
    finally: 
        requests.post(rebase_url)  

    