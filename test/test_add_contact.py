# -*- coding: utf-8 -*-
from model.contact import Contact
import time


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    time.sleep(20)  # без паузы тесты могут падать, проскакивают null

    assert len(old_contacts) + 1 == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)