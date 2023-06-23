info1 = {
    "firstname": "John",
    "lastname": "Smith",
    "totalprice": 169,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2023-06-01",
        "checkout": "2024-01-17"
    },
    "additionalneeds": "Lunch"
}
infoFail1 = {
    "firstname": "John",
    "lastname": "Smith",
    "totalprace": 169,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2023-06-01",
        "checkout": "2024-01-17"
    },
    "additionalneeds": "Lunch"
}
info2 = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}
infoPartial = {
    "firstname": "Mia",
    "lastname": "Fay",
    "totalprice": 132,
    "depositpaid": False
}
postHeader = {"Content-Type": "application/json"}

updateHeaderFail = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

deleteHeader = {
    "Content-Type": "application/json",
    "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
}
