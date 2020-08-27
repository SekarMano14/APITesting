import requests
import pytest
import flask
from requests.auth import HTTPBasicAuth


def test_get_request():
    url = "https://amazonn.atlassian.net/"
    endpoint = url + "rest/api/2/search"
    headers = {"Content-Type": "application/json"}
    get = requests.get(endpoint, headers=headers,
                       auth=HTTPBasicAuth("sekarmano95@gmail.com", "uIh5YFqooaEfzrBmbmhx3E57"))

    code = get.status_code
    print(code)
    print(get.text)


def test_post_request():
    url = "https://amazonn.atlassian.net/"
    endpoint = url + "rest/api/2/issue/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "fields": {
            "project":
                {
                    "key": "AZ"
                },
            "summary": "Create issue in Python API",
            "description": "Creating of an issue using project keys and issue type names using the Python REST API",
            "issuetype": {
                "name": "Bug"
            }
        }
    }
    get = requests.post(endpoint, headers=headers, json=payload,
                        auth=HTTPBasicAuth("sekarmano95@gmail.com", "uIh5YFqooaEfzrBmbmhx3E57"))

    code = get.status_code
    print(code)
    print(get.text)


#
def test_put_request():
    url = "https://amazonn.atlassian.net/"
    endpoint = url + "rest/api/2/issue/AZ-5"
    headers = {"Content-Type": "application/json"}
    payload = {
        "fields": {
            "summary": "Update Summary",
            "description": "update Description"
        }
    }
    get = requests.put(endpoint, headers=headers, json=payload,
                       auth=HTTPBasicAuth("sekarmano95@gmail.com", "uIh5YFqooaEfzrBmbmhx3E57"))

    code = get.status_code
    print(code)
    print(get.text)

def test_delete_request():
    url = "https://amazonn.atlassian.net/"
    endpoint = url + "rest/api/3/issue/AZ-6"
    headers = {"Content-Type": "application/json"}
    get = requests.put(endpoint, headers=headers,
                       auth=HTTPBasicAuth("sekarmano95@gmail.com", "uIh5YFqooaEfzrBmbmhx3E57"))

    code = get.status_code
    print(code)
    print(get.text)

