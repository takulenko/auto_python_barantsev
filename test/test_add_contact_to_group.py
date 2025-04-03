import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group for add"))
    groups = orm.get_group_list()
    group = random.choice(groups)

    print()
    print(groups)
    print(group)

    if len(orm.get_contacts_not_in_group(Group(id=group.id))) == 0:
        app.contact.add_contact(Contact(firstname="fn for add", lastname="ln for add"))
    contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts)

    print()
    print(contacts)
    print(contact)

    app.contact.add_contact_to_group(contact.id, group.id)
    new_contacts = orm.get_contacts_in_group(Group(id=group.id))

    print()
    print(new_contacts)

    assert contact in new_contacts
