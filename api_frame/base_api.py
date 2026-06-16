import requests 

class BaseApi: 
    
    def __init__(self, session=None):
        
        self.url = 'http://localhost:8000' 
        self.session = session or requests.Session()  
       
    
    def send_request(self, method, endpoint, **kwargs): 
        
        url = f'{self.url}{endpoint}' 
        response = self.session.request(method, url, **kwargs) 
        return response 
    
    def set_token(self, token):
        
        self.session.headers.update({"Authorization": f"Bearer {token}"}) 

    
    def get(self, endpoint, **kwargs):  
    
        return self.send_request("GET", endpoint, **kwargs)  
    
    def post(self, endpoint, **kwargs): 
        return self.send_request("POST", endpoint, **kwargs)  
    
    def delete(self, endpoint, **kwargs): 
        return self.send_request("delete", endpoint, **kwargs)  
    
    def put(self, endpoint, **kwargs): 
        return self.send_request("put", endpoint, **kwargs)  
    
    def patch(self, endpoint, **kwargs): 
        return self.send_request("patch", endpoint, **kwargs)  