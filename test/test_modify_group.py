from model.group import Group

def test_modify_group_name (app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Only Name modify"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="Only header modify"))
    app.session.logout()


def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="Only footer modify"))
    app.session.logout()
