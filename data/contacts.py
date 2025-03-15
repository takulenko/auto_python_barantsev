from model.contact import Contact
import random
import string

testdata =[
    Contact(firstname="fn1", middlename="mn1", lastname="ln1", nickname="nn1",
            title="t1", company="c1", address="a1", home="1", mobile="1", work="1",
            fax="1", email="e1", email2="e21", email3="e31", homepage="h1",
            bday="1", bmonth="January", byear="1", aday="1", amonth="January", ayear="1"),
    Contact(firstname="fn2", middlename="mn2", lastname="ln2", nickname="nn2",
            title="t2", company="c2", address="a2", home="2", mobile="2", work="2",
            fax="2", email="e2", email2="e22", email3="e32", homepage="h2",
            bday="2", bmonth="February", byear="2", aday="2", amonth="February", ayear="2"),
]


'''
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10     # + string.punctuation   ' падает
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    return random.randrange(maxlen)

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return ("".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@"
            + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "."
            + "".join([random.choice(symbols) for i in range(random.randrange(4))]))

def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return random.choice(months)

testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                title="", company="", address="", home="", mobile="", work="",
                fax="", email="", email2="", email3="", homepage="",
                bday="", bmonth="", byear="", aday="", amonth="", ayear="")] + [
    Contact(firstname=random_string("fn ", 20),
            middlename=random_string("mn ", 20),
            lastname=random_string("ln ", 20),
            nickname=random_string("fn ", 20),
            title=random_string("t ", 20),
            company=random_string("c ", 20),
            address=random_string("a ", 30),
            home=str(random_number(1000000)),
            mobile=str(random_number(1000000)),
            work=str(random_number(1000000)),
            fax=str(random_number(1000000)),
            email=random_email(10),
            email2=random_email(10),
            email3=random_email(10),
            homepage=random_string("a ", 30),
            bday=random_number(31),
            bmonth=random_month(),
            byear=str(random_number(50) + 1950),
            aday=random_number(31),
            amonth=random_month(),
            ayear=str(random_number(75) + 1950))
    for i in range(2)
]
'''