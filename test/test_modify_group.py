import random
from model.group import Group

def test_modify_group_name (app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group for modify name"))

    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(name="Only Name modify")
    app.group.edit_group_by_id(group_random.id, group)
    assert len(old_groups) == app.group.count()

    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_random)] = group
    assert old_groups == new_groups

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


'''
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
'''