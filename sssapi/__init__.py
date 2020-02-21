import requests

class Client(object):
    BASE_URL = "https://api.snowshoestamp.com/v3/"
    api_key = None

    def __init__(self, api_key=None):
        self.api_key = api_key
    
    def get_api_url(self, method):
        return "%s%s" % (self.BASE_URL, method)
    
    def call(self, data=None, method="stamp"):
        json = "{\"data\":%s}" % (data)
        response = requests.post(self.get_api_url(method=method), 
                                 data=json, headers={"SnowShoe-Api-Key":self.api_key, "Accept-Encoding":"identity", "Content-Type":"application/json"})
        
        if response.status_code >= 500:
            return {"error": "Server error while contacting %s. Data: %s" % (
                self.get_api_url(method=method), str(json)),
                    "code": 20}
        else:
            return response.json()
