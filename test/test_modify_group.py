from model.group import Group

def test_modify_group_name (app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for modify name"))
    app.group.edit_first_group(Group(name="Only Name modify"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for modify header"))
    app.group.edit_first_group(Group(header="Only header modify"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for modify footer"))
    app.group.edit_first_group(Group(footer="Only footer modify"))
