from model.group import Group

def test_modify_group_name (app):
    app.group.edit_first_group(Group(name="Only Name modify"))


def test_modify_group_header(app):
    app.group.edit_first_group(Group(header="Only header modify"))


def test_modify_group_footer(app):
    app.group.edit_first_group(Group(footer="Only footer modify"))
