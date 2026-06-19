from faker import Faker

fake = Faker()  

class Genetator: 
    
        username = fake.bothify(text='user_########') 
        email = fake.email() 
        password = fake.password() 
        display_name = fake.name()