import re

def test_phones_on_home_page(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.home == clear(contact_from_edit_page.home)
    assert contact_from_homepage.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_homepage.work == clear(contact_from_edit_page.work)

def test_phones_on_contact_view_page(app):
    contact_from_viewpage = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_viewpage.home == contact_from_edit_page.home
    assert contact_from_viewpage.mobile == contact_from_edit_page.mobile
    assert contact_from_viewpage.work == contact_from_edit_page.work

def clear(s):
    return re.sub("[() -]", "", s)
