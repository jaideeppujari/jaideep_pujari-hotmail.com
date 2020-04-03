import requests
import sys
from requests.auth import HTTPBasicAuth


  
class runLogger():

  def __init__(self):
    
    self.pdpurl = 'https://sxxx'
    print('self.pdpurl =',self.pdpurl)
   
  def run(self):
    payload = {"input":{}}
    response2 = requests.post(
    self.pdpurl,auth=HTTPBasicAuth('id', 'pwd'),json=payload,headers={'Content-Type': 'application/json','Accept': 'application/json'})
    print('response=',response2.headers)
    print('response.text=',response2.text)
    print('response.json=',response2.status_code)
    return response2.text

if __name__ == "__main__":
  q = runLogger().run()
  print(q)
