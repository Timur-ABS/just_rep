import time

import requests
import bcrypt

# url = "http://127.0.0.1:8000/authentication/registration"
# data = {
#     "email": "timurkaabs@gmail.com",
#     "login": "TimurABS",
#     "password": "your_password",
#     "referral_name": "REF"
# }
#
# response = requests.post(url, json=data)
#
# print(response.status_code)
# print(response.json())

url = "http://127.0.0.1:8000/asdf"
t1 = time.time()
for i in range(500):
    response = requests.get(url)
    k = (response.status_code)
    f = (response.json())
print(time.time() - t1)
