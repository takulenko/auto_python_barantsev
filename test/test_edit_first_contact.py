
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="First_name Edited", middlename="Middle_name Edited",
                                           lastname="Last_name Edited", nickname="Nick Edited",
                                           photo="C:/photo.jpg", title="t Edited", company="c Edited", address="a Edited",
                                           phonehome="123111111", mobile="11111", phonework="121111111",
                                           fax="13", email="contact_Edited@mail.ru", email2="22 Edited",
                                           email3="33 Edited", homepage="hp Edited",
                                           bday="11", bmonth="March", byear="1990",
                                           aday="22", amonth="May", ayear="1999"))
    app.session.logout()

