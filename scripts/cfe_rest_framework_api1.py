from requests import request
from json import dumps
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def do1(method='get', data={}, id=5):
#     r = request(method, ENDPOINT + "?id=" + str(id), data=data)
#     print(r.text)
#     return r
# do(data={'id': 12})  #  b'id=12'


def do2(method='get', data={}, id=5, is_json=True):
    if is_json:
        data = dumps(data)
    r = request(method, ENDPOINT + "?id=" + str(id), data=data)
    print(r.text)
    return r
do2(method='get', id=5)  #  b'{"id": 12}'


# def do3(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = dumps(data)
#     r = request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

image_path = os.path.join("/home/valentyn/Pictures/", "game1.jpeg")  #  "index.png"
# img_path = os.path.join(os.path.dirname(BASE_DIR), 'static-server', 'media-root/game1.jpeg')


def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = request(method, ENDPOINT, data=data, files=file_data, headers=headers)
    else:
        r = request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do_img(method='post', data={"user": 1, }, is_json=False, img_path=image_path)

# do() 

# do(method='put', data={"id": 7, "user": 1, "content": "keine deutch!"})

# do(method='put', data={"user": 1, "content": "keine deutch!"})

# do(method='delete', data={'id': 5})  