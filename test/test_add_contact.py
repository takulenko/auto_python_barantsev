# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact =  Contact(firstname="First_name", middlename="Middle_name", lastname="Last_name", nickname="Nick",
                title="t", company="c", address="a", home="123", mobile="11", work="12",
                fax="13", email="contact@mail.ru", email2="22", email3="33", homepage="hp",
                bday="10", bmonth="March", byear="1111", aday="20", amonth="May", ayear="2222")
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)