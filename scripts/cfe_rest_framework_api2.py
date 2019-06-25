from requests import request
# from json import dumps
import json
import requests
import os


# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
# REGISTER_ENDPOINT = AUTH_ENDPOINT + "register/"

# image_path = os.path.join("/home/valentyn/Pictures/", "game1.jpeg")

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "JWT " +  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo3LCJ1c2VybmFtZSI6ImJybzciLCJleHAiOjE1NjE0NjYzMjYsImVtYWlsIjoiYnJvN0BnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU2MTQ2NjAyNn0.GrK1BErmv6L64EWTNvWb-5VnncbLlnYNzERUZh1SyBQ'
# }

# data = {
#     'username': 'admin',
#     'password': 'adminadmin'
# }

# headers2 = {
#     "Content-Type": "application/json",
# }

# data2 = {
#     'username': 'dude',
#     'password': 'dudedude',
#     'password2': 'dudedude',   
# }

# data4 = {
#     'username': 'bro7',
#     'email': 'bro7@gmail.com',
#     'password': 'bro7bro7',
#     'password2': 'bro7bro7',   
# }

# AnonPermissionOnly permission check
# r4 = requests.post(REGISTER_ENDPOINT, data=json.dumps(data4), headers=headers)
# token4 = r4.json()#['token']
# print(token4)

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
id = 15
ENDPOINT = "http://127.0.0.1:8000/api/status/"
DETAIL_ENDPOINT = ENDPOINT + str(id) + "/"

image_path = os.path.join("/home/valentyn/Pictures/", "game1.jpeg")

data = {
    'username': 'admin',
    'password': 'adminadmin'
}

headers = {
    "Content-Type": "application/json",
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
# print(token)

headers2 = {
    "Authorization": "JWT " + token
}

data2 = {
    "content": "Updated description!!!"
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    # r2 = requests.put(DETAIL_ENDPOINT, data=data2, headers=headers2, files=file_data)
    # print(r2.text)
    r3 = requests.post(DETAIL_ENDPOINT, data=data2, headers=headers2, files=file_data)
    print(r3.text)