import requests
import sys
from requests.auth import HTTPBasicAuth


  
class runLogger():

  def __init__(self):
    
    self.pdpurl = 'https://sxxx'
    print('self.pdpurl =',self.pdpurl)
   

   
  def run(self):
    print('test run')


if __name__ == "__main__":
  q = runLogger().run()
  print(q)
