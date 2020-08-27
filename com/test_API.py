import requests
import pytest
import flask


def test_get_request():
    url = "https://reqres.in/api/users?page=2"
    headers = {"Content-Type": "application/json"}
    get = requests.get(url, headers=headers)

    code = get.status_code
    print(code)
    print(get.text)
    body = get.json()
    print(body["page"])
    print(body["per_page"])
    print(body["data"])


# def test_post_request():
#     url = "https://reqres.in/api/users"
#     headers = {"Content-Type": "application/json"}
#     payload = {
#         "name": "morpheus",
#         "job": "leader"
#     }
#
#     get = requests.post(url, headers=headers,json=payload)
#     code = get.status_code
#     print(code)
#     print(get.text)
#
# def test_put_request():
#     url = "https://reqres.in/api/users/2"
#     headers = {"Content-Type": "application/json"}
#     payload = {
#         "name": "morpheus",
#         "job": "TL"
#     }
#
#     get = requests.put(url, headers=headers,json=payload)
#     code = get.status_code
#     print(code)
#     print(get.text)
# def test_delete_request():
#     url = "https://reqres.in/api/users/2"
#     headers = {"Content-Type": "application/json"}
#     get = requests.delete(url, headers=headers)
#
#     code = get.status_code
#     print(code)
#     print(get.text)
#
#
#
