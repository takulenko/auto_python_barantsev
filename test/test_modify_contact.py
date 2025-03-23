from model.contact import Contact
import random


def test_modify_firstname_contact(app, db, check_ui):
    # if contacts list is empty
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="contact for modify only firstname"))

    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = Contact(firstname="Only First_name modify")
    app.contact.edit_contact_by_id(contact_random.id, contact)
    assert len(old_contacts) == app.contact.count()

    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact_random)] = contact
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

# Contact(firstname="First_name", middlename="Middle_name", lastname="Last_name", nickname="Nick",
# title="t", company="c", address="a",
# phonehome="1231", mobile="11", phonework="12111",
# fax="13", email="contact@mail.ru", email2="22", email3="33", homepage="hp",
# bday="11", bmonth="March", byear="1990", aday="22", amonth="May", ayear="1999",
# id))
