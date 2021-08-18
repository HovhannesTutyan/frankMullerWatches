import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
class Test_Login(BaseTest):
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
    def test_story_title(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_title()
    def test_story_learn_more0(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_learn_more0()
        time.sleep(2)
    def test_story_learn_more1(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_learn_more1()
        time.sleep(2)
    def test_story_learn_more2(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_learn_more2()
        time.sleep(2)
    def test_story_learn_more3(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_learn_more3()
        time.sleep(2)
    def test_story_learn_more4(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_learn_more4()
        time.sleep(2)
    def test_story_learn_more5(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_learn_more5()
        time.sleep(2)
    def test_story_learn_more6(self):
        self.story_page = LoginPage(self.driver)
        self.story_page.story_learn_more6()
        time.sleep(2)


