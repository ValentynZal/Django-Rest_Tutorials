from requests import request
from json import dumps

ENDPOINT = "http://127.0.0.1:8000/api/status/"


# def do(method='get', data={}, id=5):
#     r = request(method, ENDPOINT + "?id=" + str(id), data=data)
#     print(r.text)
#     return r
# do(data={'id': 12})  #  b'id=12'

# def do(method='get', data={}, id=5, is_json=True):
#     if is_json:
#         data = dumps(data)
#     r = request(method, ENDPOINT + "?id=" + str(id), data=data)
#     print(r.text)
#     return r
# do(data={'id': 12})  #  b'{"id": 12}'

def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = dumps(data)
    r = request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do(data={'id': 500}) 

# do(method='put', data={"id": 7, "user": 1, "content": "keine deutch!"})

# do(method='put', data={"user": 1, "content": "keine deutch!"})

do(method='delete', data={'id': 17})  