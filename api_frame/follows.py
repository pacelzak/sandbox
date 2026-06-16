from api_frame.base_api import BaseApi 
import requests 

class Follows(BaseApi): 
    
    def follow_user(self, username=None): 
        
        """Подписка на юзера"""
        return self.post(f"/api/users/{username}/follow") 
    
    def unfollow_user(self, username=None): 
        
        """Отписка от юзера"""
        return self.delete(f"/api/users/{username}/follow") 
    
    def get_follow_requests(self, page=None, per_page=None): 
         
        params = {"page": page, "per_page": per_page}
        return self.get("/api/follows/requests", params=params) 
    
    def accept_follow_requests(self, follow_id=None): 
        
        """Принятие запроса"""
        return self.post(f"/api/follows/requests/{follow_id}/accept") 
    
    def reject_follow_requests(self, follow_id=None): 
        
        """"Отказ от запроса"""
        return self.post(f"/api/follows/requests/{follow_id}/reject")