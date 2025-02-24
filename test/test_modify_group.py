from model.group import Group

def test_modify_group_name (app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for modify name"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Only Name modify"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for modify header"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="Only header modify"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for modify footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="Only footer modify"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
