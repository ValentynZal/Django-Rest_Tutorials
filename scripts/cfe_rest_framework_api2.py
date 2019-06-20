from requests import request
# from json import dumps
import json
import requests
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join("/home/valentyn/Pictures/", "game1.jpeg")

headers = {
    "Content-Type": "application/json"
}

data = {
    'username': 'admin',
    'password': 'adminadmin'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
# print(token)

# refresh_data = {
#     'token': token
# }

# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()['token'] 
# print(new_token)

headers2 = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

post_data = json.dumps({"content": "Some random content"})
posted_response = requests.post(ENDPOINT, data=post_data, headers=headers2)
# print(posted_response.text)


headers3 = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    data2 = {
        "content": "New description"
    }
    json_data = json.dumps(data)
    posted_response = requests.post(ENDPOINT, data=data2, headers=headers3, files=file_data)
    # print(posted_response.text)


with open(image_path, 'rb') as image:
    file_data2 = {
        'image': image
    }
    data3 = {
        "content": "Updated description!!!"
    }
    json_data = json.dumps(data)
    posted_response = requests.put(ENDPOINT + str(24) + "/", data=data3, headers=headers3, files=file_data2)
    # print(posted_response.text)    


data4 = {
    "content": "Updated description?"
}
json_data = json.dumps(data)
posted_response = requests.put(ENDPOINT + str(24) + "/", data=data4, headers=headers3)
print(posted_response.text)    