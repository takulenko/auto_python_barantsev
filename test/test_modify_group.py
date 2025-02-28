from random import randrange
from model.group import Group

def test_modify_group_name (app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for modify name"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Only Name modify")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()

    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="group for modify header"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header="Only header modify"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="group for modify footer"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(footer="Only footer modify"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
