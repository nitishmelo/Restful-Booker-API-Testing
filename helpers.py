import requests

def returnUrl(path):
    url = 'https://restful-booker.herokuapp.com'
    return f"{url}{path}"

def create_auth_response():
    header = {"Content-Type": "application/json"}
    data = {
        "username": "admin",
        "password": "password123",
    }
    response = requests.post(returnUrl('/auth'), headers=header, json=data)
    return response

def return_booking_id():
    response = requests.get(returnUrl('/booking'))
    body = response.json()
    return body[0]['bookingid']

def getForPing(url):
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 201

def getAssertCode(url):
    response = requests.get(url)
    body = response.json()
    assert body is not None
    assert response.status_code == 200

def postAssertCode(url, headers, data):
    response = requests.post(url, headers=headers, json=data)
    body = response.json()
    assert body is not None
    assert response.status_code == 200

def putAssertCode(url, headers, data):
    response = requests.put(url, headers=headers, json=data)
    body = response.json()
    assert body is not None
    assert response.status_code == 200

def patchAssertCode(url, headers, data):
    response = requests.patch(url, headers=headers, json=data)
    body = response.json()
    assert body is not None
    assert response.status_code == 200

def deleteAssertCode(url, headers):
    response = requests.delete(url, headers=headers)
    print(response.text)
    assert response.status_code == 201

def invalidURL(url):
    response = requests.get(url)
    assert response.status_code == 404

def postInternalServerError(url, headers, data):
    response = requests.post(url, headers, data)
    assert response.status_code == 500

def putForbiddenError(url, headers, data):
    response = requests.put(url, headers=headers, json=data)
    assert response.status_code == 403