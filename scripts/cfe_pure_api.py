import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id": id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print("\n Status code: {} \n".format(r.status_code))
    status_code = r.status_code
    if status_code != 200:
        data = r.json()
    return data

# uncomment to run get_list test
# print(get_list()) 


def create_update():
    new_data = {
        'user': 1,
        "content": "Another new update"
    }
    # r = requests.delete(BASE_URL + ENDPOINT, data=new_data) 
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data)) 
    print("\n", r.headers, "\n")
    if r.status_code == requests.codes.ok:
        # print(r.json(), "\n")
        return r.json()
    return r.text

# uncomment to run create test
# print(create_update())


def do_obj_update():
    new_data = {
        "id": 1,
        "content": "New obj data"
    }
    # r = requests.delete(BASE_URL + ENDPOINT + "1/", data=new_data)     
    # r = requests.post(BASE_URL + ENDPOINT + "1/", data=new_data) 
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))  # json.dumps(new_data))
    print("\n", r.headers, "\n")
    if r.status_code == requests.codes.ok:
        # print(r.json(), "\n")
        return r.json()
    return r.text

# uncomment to run update obj test
# print(do_obj_update())


def do_obj_delete():
    new_data = {
        "id": 6
    }
    # r = requests.put(BASE_URL + ENDPOINT + "1/", data=new_data)     
    # r = requests.post(BASE_URL + ENDPOINT + "1/", data=new_data) 
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data)) # json.dumps(new_data))
    print("\n", r.headers, "\n")
    if r.status_code == requests.codes.ok:
        # print(r.json(), "\n")
        return r.json()
    return r.text

# uncomment to run delete obj test
# print(do_obj_delete())