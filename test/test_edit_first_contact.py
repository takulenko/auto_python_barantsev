from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="contact for edit"))
    app.contact.edit_first_contact(Contact(firstname="First_name Edited", middlename="Middle_name Edited",
                                           lastname="Last_name Edited", nickname="Nick Edited",
                                           title="t Edited", company="c Edited", address="a Edited",
                                           home="123111111", mobile="11111", work="121111111",
                                           fax="13", email="contact_Edited@mail.ru", email2="22 Edited",
                                           email3="33 Edited", homepage="hp Edited",
                                           bday="11", bmonth="March", byear="1990",
                                           aday="22", amonth="May", ayear="1999"))
