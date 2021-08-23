import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.WatchesPage import WatchesPage
from Tests.test_base import BaseTest
from selenium.webdriver.common.by import By
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
    # def test_collection_titles3(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.collection_titles3()
    # def test_search_by_empty_field(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.search_by_empty_field()
    #     watches = self.driver.find_elements(By.CSS_SELECTOR,".watch")
    #     assert len(watches) == 9
    # def test_search_by_prod_spec(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.search_by_prod_spec()
    #     watch_title = self.driver.find_elements(By.CSS_SELECTOR,".watch__title")
    #     for title in watch_title:
    #         if title.text == "V 45 CC GD SQT (NR)":
    #             title.click()
    #     tag_descriptions = self.driver.find_elements(By.CSS_SELECTOR,".tag__description")
    #     for desc in tag_descriptions:
    #         if "Winding shaft" in desc.text:
    #             print("********************* Search Text exists in product specifications ************************")
    #         # else:
    #         #     print("--------------------- Search text does not exist ----------------")
    # def test_search_by_collection_name(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.search_by_collection_name()
    #     skafander_watches = self.driver.find_element(By.CSS_SELECTOR,".watches")
    #     if skafander_watches.text == "globals.notFound":
    #         print("------------ The search is not working with COLLECTION NAMES ---------------")
    #     else:
    #         print(" *********** The search is working with COLLECTION NAMES ******************* ")

    # def test_search_by_sub_collection_name(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.search_by_sub_collection_name()
    #     vanguard_yachting = self.driver.find_element(By.CSS_SELECTOR,".watches")
    #     if vanguard_yachting.text == "globals.notFound":
    #         print("------------ The search is not working with SUBCOLLECTION NAMES ------------")
    #     else:
    #         print(" ************ The search is working with SUBCOLLECTION NAMES *************** ")
    # def test_search_by_product_full_name(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.search_by_product_full_name()
    #     full_name = self.driver.find_element(By.CSS_SELECTOR,".watches")
    #     # print(full_name.text[0:18])
    #     if full_name.text[0:18] == WatchesPage.SEARCH_SAMPLE_WATCH_NAME:
    #         print(" ************ The search is working with PRODUCT FULL NAME *************** ")
    #     else:
    #         print("------------ The search is not working with PRODUCT FULL NAME ------------")
    # def test_filter_by_empty_tags(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.filter_by_empty_tags()
    #     all_watches = self.driver.find_elements(By.CSS_SELECTOR,".watch")
    #     # print(len(all_watches))
    #     assert len(all_watches) == 9
    # def test_filter_delete_by_not_done(self):
    #     self.loginPage = WatchesPage(self.driver)
    #     self.loginPage.filter_delete_by_not_done()
    #     collections = self.driver.find_elements(By.CSS_SELECTOR,".collection")
    #     for collection in collections:
    #         if collection.text == "VANGUARD":
    #             print("************ After deleting the not done filter the collections page is displayed ***************")
    #     else:
    #         print("----------- All watches are displayed after deleting the not done filter --------------")
    def test_filter_by_random_tags(self):
        self.loginPage = WatchesPage(self.driver)
        self.loginPage.filter_by_random_tags()
        selected_title = self.driver.find_element(By.CSS_SELECTOR,".selected__title")
        watch_title = self.driver.find_elements(By.CSS_SELECTOR,".watch__title")
        if selected_title.text == "Ladies'":
            assert watch_title[0].text == "V 45 SC DT YACHT (BL)"
            assert watch_title[1].text == "V 45 CC GD SQT (NR)"
        elif selected_title.text == "Men's":
            assert watch_title[0].text == "V 32 QZ D (NR) ace"
            assert watch_title[1].text == "V 32 QZ D (NR)"
            assert watch_title[2].text == "V 32 QZ D CD (NR)"
            assert watch_title[3].text == "V 32 QZ D CD (NR) ace"
            assert watch_title[4].text == "V 32 QZ COL DRM D CD (RG)"
            assert watch_title[5].text == "V 35 QZ COL DRM D CD (RG)"
            assert watch_title[6].text == "2852 QZ DP O"
        elif selected_title.text == "North America Exclusives":
            assert watch_title[0].text == "V 45 SC DT YACHT (BL)"
            assert watch_title[1].text == "V 45 CC GD SQT (NR)"
        elif selected_title.text == "Gem-set":
            assert watch_title[0].text == "V 32 QZ D (NR) ace"
            assert watch_title[1].text == "V 32 QZ D (NR)"
            assert watch_title[2].text == "V 32 QZ D CD (NR)"
            assert watch_title[3].text == "V 32 QZ D CD (NR) ace"
            assert watch_title[4].text == "V 32 QZ COL DRM D CD (RG)"
            assert watch_title[5].text == "V 35 QZ COL DRM D CD (RG)"
            assert watch_title[6].text == "2852 QZ DP O"
        elif selected_title.text == "Automatic (Self-winding)":
            assert watch_title[0].text == "V 45 SC DT YACHT (BL)"
            assert watch_title[1].text == "V 45 CC GD SQT (NR)"
        elif selected_title.text == "Quartz":
            assert watch_title[0].text == "V 32 QZ D (NR) ace"
            assert watch_title[1].text == "V 32 QZ D (NR)"
            assert watch_title[2].text == "V 32 QZ D CD (NR)"
            assert watch_title[3].text == "V 32 QZ D CD (NR) ace"
            assert watch_title[4].text == "V 32 QZ COL DRM D CD (RG)"
            assert watch_title[5].text == "V 35 QZ COL DRM D CD (RG)"
            assert watch_title[6].text == "2852 QZ DP O"
        elif selected_title.text == "Chronograph":
            assert watch_title[0].text == "V 45 CC GD SQT (NR)"
        elif selected_title.text == "Grande Date":
            assert watch_title[0].text == "V 45 CC GD SQT (NR)"
        elif selected_title.text == "Stainless Steel":
            assert watch_title[0].text == "V 32 QZ D (NR) ace"
            assert watch_title[1].text == "V 32 QZ D CD (NR) ace"
            assert watch_title[2].text == "2852 QZ DP O"
        elif selected_title.text == "Stainless Steel":
            assert watch_title[0].text == "V 32 QZ D (NR) ace"
            assert watch_title[1].text == "V 32 QZ D CD (NR) ace"
            assert watch_title[2].text == "2852 QZ DP O"
        elif selected_title.text == "18K Rose Gold":
            assert watch_title[0].text == "V 32 QZ D (NR)"
            assert watch_title[1].text == "V 32 QZ D CD (NR)"
            assert watch_title[2].text == "V 32 QZ COL DRM D CD (RG)"
            assert watch_title[3].text == "V 35 QZ COL DRM D CD (RG)"
            assert watch_title[4].text == "V 45 SC DT YACHT (BL)"
            assert watch_title[5].text == "V 45 CC GD SQT (NR)"
        elif selected_title.text == "$5'000 to $15'999":
            assert watch_title[2].text == "2852 QZ DP O"
        elif selected_title.text == "$16'000 to $29'999":
            assert watch_title[0].text == "V 32 QZ D (NR) ace"
            assert watch_title[1].text == "V 32 QZ D (NR)"
            assert watch_title[2].text == "V 32 QZ D CD (NR) ace"
            assert watch_title[3].text == "V 45 SC DT YACHT (BL)"
        elif selected_title.text == "$30000 to $49'999":
            assert watch_title[0].text == "V 32 QZ D CD (NR)"
            assert watch_title[1].text == "V 32 QZ COL DRM D CD (RG)"
            assert watch_title[2].text == "V 35 QZ COL DRM D CD (RG)"
            assert watch_title[3].text == "V 45 CC GD SQT (NR)"














