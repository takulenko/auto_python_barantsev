# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(Contact(firstname="First_name", middlename="Middle_name", lastname="Last_name", nickname="Nick",
                photo="C:/photo.jpg", title="t", company="c", address="a", phonehome="123", mobile="11", phonework="12",
                fax="13", email="contact@mail.ru", email2="22", email3="33", homepage="hp",
                bday="10", bmonth="March", byear="1111", aday="20", amonth="May", ayear="2222"))
    app.session.logout()

