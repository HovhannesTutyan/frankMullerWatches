import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.WatchesPage import WatchesPage
from Tests.test_base import BaseTest
class Test_Login(BaseTest):
    def test_login(self):
        self.loginPage = WatchesPage(self.driver)
    # def test_title_check(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.title_check()
    # def test_menu_items(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.menu_items()
    # def test_collection_titles1(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.collection_titles1()
    # def test_collection_titles2(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.collection_titles2()
    def test_collection_titles3(self):
        self.loginPage = WatchesPage(self.driver)
        self.loginPage.collection_titles3()
