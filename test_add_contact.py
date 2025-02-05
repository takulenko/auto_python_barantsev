# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_base_url(wd)
        self.login(wd)
        self.add_contact(wd)
        self.go_home_page(wd)

    def open_base_url(self, wd):
        wd.get("https://localhost/addressbook/")

    def go_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_contact(self, wd, contact_firstname="First_name", contact_middlename="Middle_name", contact_lastname="Last_name",
                    contact_nickname="Nick", contact_phonehome="123", contact_email="contact@mail.ru", contact_bday="1",
                    contact_bmonth="February", contact_byear="2002", contact_photo="photo.jpg", contact_title="11",
                    company="11", company_address="11", contact_mobile="11", contact_phonework="11", contact_fax="11",
                    contact_email2="11", contact_email3="11", contact_homepage="11", contact_aday="26",
                    contact_amonth="November", contact_ayear="2010"):
        # init contact creation
        wd.find_element_by_link_text("add new").click()

        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact_middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact_nickname)

        wd.find_element_by_name("photo").clear()
#        wd.find_element_by_name("photo").send_keys(contact_photo)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact_title)

        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(company_address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_phonehome)

        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact_phonework)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact_fax)

        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact_email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact_email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact_homepage)


        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact_bday)
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact_bmonth)
        wd.find_element_by_xpath("//option[@value='February']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact_byear)

        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact_aday)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[28]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact_amonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[12]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact_ayear)

        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
