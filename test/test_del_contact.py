import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    # if contacts list is empty
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="contact for delete"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()

    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
