import pytest 
import requests

def assert_status_code(response, except_code): 
    
    actual_code = response.status_code 
    
    assert actual_code == except_code, f"ответ сервера {response.text}, {response.status_code}"  

def assert_message(response, except_message): 
    
    actual_message = response.reason 
    
    assert actual_message == except_message, f"{response.reason}" 

def assert_headers(response, excerpt_header, value_headers): 
    """Проверка заголовка"""
    value = response.headers.get(excerpt_header)
    assert value == value_headers, (response.headers)
    
def assert_json_value(response, key, expected_value):
    """Проверка конкретного ключа"""
    try:
        json_data = response.json()
    except ValueError:
        assert False, f"Ответ сервера не является JSON. Текст ответа: {response.text}"
        
    actual_value = json_data.get(key)
    assert actual_value == expected_value, (
        f"В ключе '{key}' ожидали '{expected_value}', но получили '{actual_value}'"
    )

def assert_response_time(response, max_time_seconds):
    """Проверяет, что сервер ответил быстрее, чем за X секунд."""
    # .total_seconds() возвращает float (например, 0.23)
    actual_time = response.elapsed.total_seconds()
    assert actual_time <= max_time_seconds, (
        f"Запрос шел слишком долго: {actual_time} сек. (Максимум: {max_time_seconds} сек.)"
    ) 

def assert_json_value_type(response, key, expected_type):
    """Проверяет, что поле в JSON имеет определенный тип (str, int, list и т.д.)."""
    json_data = response.json()
    actual_value = json_data.get(key)
    
    assert isinstance(actual_value, expected_type), (
        f"Поле '{key}' имеет тип {type(actual_value).__name__}, а ожидали {expected_type.__name__}"
    ) 

def assert_has_keys(response, expected_keys: list):
    """Проверяет, что все указанные ключи присутствуют в корне JSON."""
    json_data = response.json()
    # Находим, каких ключей не хватает в ответе
    missing_keys = [key for key in expected_keys if key not in json_data]
    
    assert not missing_keys, f"В ответе отсутствуют обязательные ключи: {missing_keys}"
