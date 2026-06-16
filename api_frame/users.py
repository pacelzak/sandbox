from api_frame.base_api import BaseApi 
import requests

class Users(BaseApi):
    
    
    def list_users(self, search=None, sort_by=None, sort_order=None, page=None, per_page=None):
        """Список пользователей"""
        params = {
            "search": search, 
            "sort_by": sort_by, 
            "sort_order": sort_order,
            "page": page, 
            "per_page": per_page
        }
     
        return self.get("/api/users", params=params)
    
    def get_suggestions(self): 
        
        """5 наиболее активных пользователей, на которых мы не подписанны""" 
        
        return self.get("/api/users/suggestions") 
    
    def get_user(self, username=None): 
        
        """Конкретный пользователь"""
        
        return self.get(f"/api/users/{username}") 

    def update_me(self, display_name=None, bio=None, is_private=None): 
        
        """Обновление информации провиля"""
        
        data = {"display_name": display_name, "bio": bio, "is_private": is_private} 
        return self.patch("/api/users/me", json=data) 
    
    def update_avatar(self, file): 
        
        with open(f"{file}", 'rb') as img:
            files = {'file': ('my_photo.jpg', img, 'image/jpeg')} 
            return self.post('/api/users/me/avatar', files=files) 
            
    
    def delete_avatar(self): 
        
        """Удаления аватара пользователя""" 
        
        return self.delete("/api/users/me/avatar")  
    
    def get_user_post(self, username=None , page=None, per_page=None): 
        
        """Список постов пользователя"""
         
        params = {"page": page, "per_page": per_page}
        return self.get(f"/api/users/{username}/posts", params=params) 
    
    
    def get_followers(self, username=None , page=None, per_page=None): 
        
        params = {"page": page, "per_page": per_page}
        return self.get(f"/api/users/{username}/followers") 
    
    
    def get_following(self, username=None , page=None, per_page=None): 
        
        params = {"page": page, "per_page": per_page}
        return self.get(f"/api/users/{username}/following")