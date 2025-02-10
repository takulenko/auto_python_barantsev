# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from application import Application
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("qwe", "asd", "zxc"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("", "", ""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()