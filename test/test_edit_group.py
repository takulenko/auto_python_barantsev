from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="qwe Edited", header="asd Edited", footer="zxc Edited"))
    app.session.logout()

