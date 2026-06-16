from faker import Faker

fake = Faker()  

class Genetator: 
    
        # Используем slug или просто фильтруем символы
        # Метод .bothify генерирует строку по шаблону (???????? - 8 случайных букв)
        username = fake.bothify(text='user_########') 
        email = fake.email() 
        password = fake.password() 
        display_name = fake.name()