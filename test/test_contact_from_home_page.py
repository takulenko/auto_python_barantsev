from model.contact import Contact
from random import randrange
import re

def test_contact_on_home_page_by_index(app):
    # if contacts list is empty
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(lastname="Ak-ul", firstname="Tata Rastata", address="Addr H: 1",
                                        email="em@m.ru", email2="em2@m.ru", email3="em3@m.ru",
                                        home="home-1231", mobile="(mobile) 11", work="work 12111"))

    contacts_list_from_homepage = app.contact.get_contact_list()
    index = randrange(len(contacts_list_from_homepage))

    contact_from_homepage = contacts_list_from_homepage[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
