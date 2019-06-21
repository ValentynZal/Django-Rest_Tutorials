from requests import request
# from json import dumps
import json
import requests
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REGISTER_ENDPOINT = AUTH_ENDPOINT + "register/"

image_path = os.path.join("/home/valentyn/Pictures/", "game1.jpeg")

headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTYxMTA0NjQyLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTYxMTA0MzQyfQ.o8R0FXZl3WgmeceG9FtAXY60Avy-1awwXagtBCyYqxs'
}

data = {
    'username': 'admin',
    'password': 'adminadmin'
}

headers2 = {
    "Content-Type": "application/json",
}

data2 = {
    'username': 'dude',
    'password': 'dudedude',
    'password2': 'dudedude',   
}

data3 = {
    'username': 'bro',
    'email': 'bro@gmail.com',
    'password': 'brobro',
    'password2': 'bro',   
}

data4 = {
    'username': 'bro',
    'email': 'bro@gmail.com',
    'password': 'brobro',
    'password2': 'brobro',   
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
r2 = requests.post(REGISTER_ENDPOINT, data=json.dumps(data2), headers=headers2)
r3 = requests.post(REGISTER_ENDPOINT, data=json.dumps(data3), headers=headers2)
r4 = requests.post(REGISTER_ENDPOINT, data=json.dumps(data4), headers=headers2)
# token = r.json()#['token']
# print(token)
# token2 = r2.json()#['token']
# print(token2)
# token3 = r3.json()#['token']
# print(token3)
token4 = r4.json()#['token']
print(token4)


