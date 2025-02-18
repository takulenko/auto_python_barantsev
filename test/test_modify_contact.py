from model.contact import Contact

def test_modify_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="contact for modify only firstname"))
    app.contact.edit_first_contact(Contact(firstname="Only First_name modify"))



# Contact(firstname="First_name", middlename="Middle_name", lastname="Last_name", nickname="Nick",
# title="t", company="c", address="a",
# phonehome="1231", mobile="11", phonework="12111",
# fax="13", email="contact@mail.ru", email2="22", email3="33", homepage="hp",
# bday="11", bmonth="March", byear="1990", aday="22", amonth="May", ayear="1999"))
