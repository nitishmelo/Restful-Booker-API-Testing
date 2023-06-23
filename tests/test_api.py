import pytest
import helpers
import data

def test_create_auth_token():
    assert helpers.create_auth_response().status_code == 200

def test_get_booking_ids():
    helpers.getAssertCode(helpers.returnUrl('/booking'))
    helpers.getAssertCode(
        helpers.returnUrl('/booking?firstname=sally&lastname=brown'))
    helpers.getAssertCode(
        helpers.returnUrl('/booking?checkin=2014-03-13&checkout=2014-05-21'))

def test_get_booking_ids_fail():
    helpers.invalidURL(helpers.returnUrl('/bookign'))

def test_get_booking_with_ID():
    helpers.getAssertCode(
        helpers.returnUrl(f'/booking/{helpers.return_booking_id()}'))

def test_get_booking_with_ID_fail():
    helpers.invalidURL(helpers.returnUrl('/booking/-1'))

def test_create_booking():
    helpers.postAssertCode(helpers.returnUrl('/booking'), data.postHeader,
                           data.info1)

def test_create_booking_fail():
    helpers.invalidURL(helpers.returnUrl('/Sooking'))
    helpers.postInternalServerError(helpers.returnUrl('/booking'),
                                    data.postHeader, data.infoFail1)

def test_update_booking():
    token = helpers.create_auth_response().json()['token']
    updateHeader = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    helpers.putAssertCode(
        helpers.returnUrl(f'/booking/{helpers.return_booking_id()}'),
        updateHeader, data.info2)

def test_update_booking_fail():
    helpers.putForbiddenError(
        helpers.returnUrl(f'/booking/{helpers.return_booking_id()}'),
        data.postHeader, data.info2)

def test_partial_update_booking():
    token = helpers.create_auth_response().json()['token']
    updateHeader = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    helpers.patchAssertCode(
        helpers.returnUrl(f'/booking/{helpers.return_booking_id()}'),
        updateHeader, data.infoPartial)

def test_partial_update_booking_fail():
    helpers.putForbiddenError(
        helpers.returnUrl(f'/booking/{helpers.return_booking_id()}'),
        data.updateHeaderFail, data.info2)

def test_delete_booking():
    helpers.deleteAssertCode(
        helpers.returnUrl(f'/booking/{helpers.return_booking_id()}'),
        data.deleteHeader)

def test_delete_booking_fail():
    helpers.invalidURL(
        helpers.returnUrl('/booking/-1'))

def test_health():
    helpers.getForPing(helpers.returnUrl('/ping'))