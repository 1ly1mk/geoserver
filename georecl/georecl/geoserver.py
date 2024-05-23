from requests import Session,PreparedRequest
from requests.auth import AuthBase


class GeoserverAuth1(AuthBase):
    def __init__(self,username=None,password=None,authkey=None) -> None:
        super().__init__()
        self.username=username
        self.password=password
        self.authkey=authkey
    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        if self.username and self.password:
            r.prepare_auth((self.username,self.password),r.url)
        elif self.authkey:
            r.prepare_url(r.url,{"authkey":self.authkey})
        else:
            raise ValueError("No credentials provided")
        return r

class GeoserverAuth(AuthBase):
    def __init__(self, auth:tuple=None,authkey:str=None):
        super().__init__()
        self.auth=auth
        self.authkey=authkey
    def __call__(self, r):       
        print(self.auth)
        if self.auth:
            r.prepare_auth(self.auth,r.url)
        elif self.authkey:
            r.prepare_url(r.url,{"authkey":self.authkey})
        else:
            raise ValueError("No credentials provided")        
        print("auth called)")
        return r
    
class Geoserver(Session):
    def __init__(self,url:str,username:str=None,password:str=None,authkey:str=None,format:str="xml") -> None:
        super().__init__()
        self.format=format
        self.base_url=url
        self.auth=GeoserverAuth1(username,password,authkey)
    def set_format(self,format:str):
        self.format=format
        
    def get_status(self):
        url=f'{self.base_url}/rest/about/version.{self.format}'
        return self.get(url)
        
    