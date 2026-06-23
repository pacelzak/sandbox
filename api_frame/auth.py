from api_frame.base_api import BaseApi 

class Auth(BaseApi):  
    
    def register(self, email=None, username=None, password=None, display_name=None): 
        
        """"Метод для регистрации""" 
        
        data = {"email": email, 
                "username": username, 
                "password": password, 
                "display_name": display_name}
        return self.post("/api/auth/register", json=data)      
    
    def login(self, email=None, password=None): 
        
        """Метод для авторизации""" 
        
        data = {"email": email, 
                "password": password}  
        return self.post("/api/auth/login", json=data)  
    
    def refresh(self, refresh_token=None): 
        
        """Обновление токена""" 
        
        data = {"refresh_token": refresh_token} 
        return self.post("/api/auth/refresh", json=data)  

    def logout(self, refresh_token=None): 
        
        """Выход из аккаунта"""  
        
        data = {"refresh_token": refresh_token} 
        return self.post("/api/auth/logout", json=data)  
    
    def get_me(self):  
        
        """Информация о своем аккаунте""" 
        
        return self.get("/api/auth/me")  
        
    
    