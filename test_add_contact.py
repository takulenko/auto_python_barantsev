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
        wd.get("https://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("My name")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Middle_name")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Last_name")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Nick")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("123")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("contact@mail.ru")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("February")
        wd.find_element_by_xpath("//option[@value='February']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2002")
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        wd.find_element_by_link_text("home").click()
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
