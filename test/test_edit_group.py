import random
from model.group import Group

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group for edit"))

    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(name="qwe Edited", header="asd Edited", footer="zxc Edited")
    app.group.edit_group_by_id(group_random.id, group)
    assert len(old_groups) == app.group.count()

    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_random)] = group
    assert old_groups == new_groups

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
