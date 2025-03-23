from model.contact import Contact
import random

def test_edit_contact_by_index(app, db, check_ui):
    # if contacts list is empty
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="contact for edit"))

    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = Contact(firstname="First_name Edited", middlename="Middle_name Edited",
                      lastname="Last_name Edited", nickname="Nick Edited",
                      title="t Edited", company="c Edited", address="a Edited",
                      home="123111111", mobile="11111", work="121111111",
                      fax="13", email="contact_Edited@mail.ru", email2="22 Edited",
                      email3="33 Edited", homepage="hp Edited",
                      bday="11", bmonth="March", byear="1990",
                      aday="22", amonth="May", ayear="1999")
    app.contact.edit_contact_by_id(contact_random.id, contact)
    assert len(old_contacts) == app.contact.count()

    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact_random)] = contact
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
