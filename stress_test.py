import time
import requests
from threading import *

url = "http://127.0.0.1:8000/authentication/registration"
x1 = time.time()
for i in range(500):
    print(requests.post(url, json={'login': 'TimurABS', 'email': 'timurkaabs@gmail.com', 'password': '123',
                                   'referral_name': ''}).json())
print(time.time() - x1)
