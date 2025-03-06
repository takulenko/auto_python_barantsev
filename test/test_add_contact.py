# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import time

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10     # + string.punctuation   ' падает
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    return random.randrange(maxlen)

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return ("".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@"
            + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "."
            + "".join([random.choice(symbols) for i in range(random.randrange(4))]))

def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return random.choice(months)

testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                title="", company="", address="", home="", mobile="", work="",
                fax="", email="", email2="", email3="", homepage="",
                bday="", bmonth="", byear="", aday="", amonth="", ayear="")] + [
    Contact(firstname=random_string("fn ", 20),
            middlename=random_string("mn ", 20),
            lastname=random_string("ln ", 20),
            nickname=random_string("fn ", 20),
            title=random_string("t ", 20),
            company=random_string("c ", 20),
            address=random_string("a ", 30),
            home=str(random_number(1000000)),
            mobile=str(random_number(1000000)),
            work=str(random_number(1000000)),
            fax=str(random_number(1000000)),
            email=random_email(10),
            email2=random_email(10),
            email3=random_email(10),
            homepage=random_string("a ", 30),
            bday=random_number(31),
            bmonth=random_month(),
            byear=str(random_number(50) + 1950),
            aday=random_number(31),
            amonth=random_month(),
            ayear=str(random_number(75) + 1950))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    time.sleep(10)  # без паузы тесты могут падать, проскакивают null

    assert len(old_contacts) + 1 == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)