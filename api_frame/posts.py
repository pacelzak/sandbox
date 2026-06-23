from api_frame.base_api import BaseApi 

class Posts(BaseApi): 
    
    def get_list_posts(self, hashtag=None, author_id=None, sort_by=None, sort_order=None, page=None, per_page=None): 
        
        """Список постов"""
        
        params = {"hashtag": hashtag, "author_id": author_id, "sort_by" : sort_by, "sort_order" : sort_order, "page" : page, 
                  "per_page" : per_page} 
        return self.get("/api/posts", params=params) 
    
    def create_post(self, content=None, image_url=None, visibility=None): 
        
        """Создание поста"""
        
        body = {
                "content": content,
                "image_url": image_url,
                "visibility": visibility
                } 
        return self.post("/api/posts", json=body)