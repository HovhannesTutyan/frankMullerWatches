from Config.config import TestData
from Pages.BasePage import BasePage
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randint

class WatchesPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search__input")
    SEARCH_SAMPLE_WATCH_NAME = "V 32 QZ D (NR) ace"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://fm.awi.am/watches')
        time.sleep(10)
        self.driver.maximize_window()
        time.sleep(2)
    def title_check(self):
        get_title = self.driver.title
        # print(get_title)
        assert get_title == "Franck Muller USA"
    def menu_items(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR,".menu__item  ")
        # for item in menu_items:
        #     print(item.text)
        assert menu_items[0].text == "THE STORY"
        assert menu_items[1].text == "THE WATCHES"
        assert menu_items[2].text == "NORTH AMERICA EXCLUSIVES"
        assert menu_items[3].text == "NEWS"
        assert menu_items[4].text == "BOUTIQUES"
        assert menu_items[5].text == "MY FRANCK MULLER"
        assert menu_items[6].text == "CONTACT US"
        assert menu_items[7].text == "Gender"
        assert menu_items[8].text == "North America Exclusives"
        assert menu_items[9].text == "Gem-set"
        assert menu_items[10].text == "Mechanism"
        assert menu_items[11].text == "Feature / Complication"
        assert menu_items[12].text == "Case Material"
        assert menu_items[13].text == "Price"
    def collection_titles1(self):
        collection_titles = self.driver.find_elements(By.CSS_SELECTOR,".collection__title")
        # for collection in collection_titles:
        #     print(collection.text)
        assert collection_titles[0].text == "VANGUARD"
        assert collection_titles[1].text == "VANGUARD LADY"
        assert collection_titles[2].text == "CINTRÉE CURVEX"
        assert collection_titles[3].text == "ROUND"
        assert collection_titles[4].text == "LONG ISLAND"
        assert collection_titles[5].text == "MASTER SQUARE"
        assert collection_titles[6].text == "SKAFANDER"
        assert collection_titles[7].text == "AETERNITAS"
        assert len(collection_titles) == 8
    def collection_titles2(self):
        pagination = self.driver.find_elements(By.CSS_SELECTOR,".list__item")
        pagination[1].click()
        collection_titles = self.driver.find_elements(By.CSS_SELECTOR,".collection__title")
        # for collection in collection_titles:
        #     print(collection.text)
        assert collection_titles[0].text == "REVOLUTION / EVOLUTION"
        assert collection_titles[1].text == "FAST TOURBILLON"
        assert collection_titles[2].text == "GIGA TOURBILLON"
        assert collection_titles[3].text == "PERPETUAL CALENDAR"
        assert collection_titles[4].text == "TOURBILLON MINUTE REPEATER SKELETON"
        assert collection_titles[5].text == "GRAVITY"
        assert collection_titles[6].text == "GRAND CENTRAL TOURBILLON"
        assert collection_titles[7].text == "GALET"
        assert len(collection_titles) == 8
    def collection_titles3(self):
        pagination = self.driver.find_elements(By.CSS_SELECTOR,".list__item")
        pagination[2].click()
        collection_titles = self.driver.find_elements(By.CSS_SELECTOR,".collection__title")
        # for collection in collection_titles:
        #     print(collection.text)
        assert collection_titles[0].text == "HEART"
        assert collection_titles[1].text == "INFINITY"
        assert collection_titles[2].text == "CIELO"
        assert len(collection_titles) == 3
    def search_by_empty_field(self):
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT,Keys.ENTER)
    def search_by_prod_spec(self):
        self.do_click(self.SEARCH_INPUT)
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT,"Winding shaft")
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT,Keys.ENTER)
        time.sleep(2)
    def search_by_collection_name(self):                 ################### BUG ###################
        self.do_click(self.SEARCH_INPUT)
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT, "SKAFANDER")
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT, Keys.ENTER)
        time.sleep(2)
    def search_by_sub_collection_name(self):            ################## BUG ####################
        self.do_click(self.SEARCH_INPUT)
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT, "Vanguard Yachting")
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT, Keys.ENTER)
        time.sleep(2)
    def search_by_product_full_name(self):
        self.do_click(self.SEARCH_INPUT)
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT, self.SEARCH_SAMPLE_WATCH_NAME)
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT, Keys.ENTER)
        time.sleep(2)
    def filter_by_empty_tags(self):
        menu_item = self.driver.find_elements(By.CSS_SELECTOR,".menu__item")
        for item in menu_item:
            if item.text == "Gender":
                item.click()
        filter_done = self.driver.find_elements(By.CSS_SELECTOR,".group__search.button")
        time.sleep(2)
        filter_done[0].click()
    def filter_delete_by_not_done(self):                                                                ############# BUG #############
        menu_item = self.driver.find_elements(By.CSS_SELECTOR, ".menu__item")
        def gender_click():
            for item in menu_item:
                if item.text == "Gender":
                    item.click()
        gender_click()
        filter_checkbox = self.driver.find_elements(By.CSS_SELECTOR,".group__checkbox")
        time.sleep(3)
        filter_checkbox[0].click()
        time.sleep(3)
        gender_click()
        time.sleep(3)
        filter_close = self.driver.find_element(By.CSS_SELECTOR,".selected__item")
        filter_close.click()
        time.sleep(5)
    def filter_by_random_tags(self):
        menu_item = self.driver.find_elements(By.CSS_SELECTOR, ".menu__item")
        filter_list = [menu_item[7],menu_item[8],menu_item[9],menu_item[10],menu_item[11],menu_item[12],menu_item[13]]
        i = filter_list[randint(0, len(filter_list)-1)]
        i.click()
        time.sleep(2)
        group_item = self.driver.find_elements(By.CSS_SELECTOR,".group__item  ")
        filter_done = self.driver.find_elements(By.CSS_SELECTOR, ".group__search.button")
        subfilter_list1 = [group_item[0],group_item[1]]
        subfilter_list2 = [group_item[2]]
        subfilter_list3 = [group_item[3]]
        subfilter_list4 = [group_item[4], group_item[5]]
        subfilter_list5 = [group_item[6], group_item[7]]
        subfilter_list6 = [group_item[8], group_item[9]]
        subfilter_list7 = [group_item[10], group_item[11], group_item[12]]
        if i == filter_list[0]:
            subfilter_list1[randint(0,len(subfilter_list1)-1)].click()
            time.sleep(2)
            filter_done[0].click()
        elif i == filter_list[1]:
            subfilter_list2[randint(0,len(subfilter_list2)-1)].click()
            time.sleep(2)
            filter_done[1].click()
        elif i == filter_list[2]:
            subfilter_list3[randint(0,len(subfilter_list3)-1)].click()
            time.sleep(2)
            filter_done[2].click()
        elif i == filter_list[3]:
            subfilter_list4[randint(0,len(subfilter_list4)-1)].click()
            time.sleep(2)
            filter_done[3].click()
        elif i == filter_list[4]:
            subfilter_list5[randint(0,len(subfilter_list5)-1)].click()
            time.sleep(2)
            filter_done[4].click()
        elif i == filter_list[5]:
            subfilter_list6[randint(0,len(subfilter_list6)-1)].click()
            time.sleep(2)
            filter_done[5].click()
        elif i == filter_list[6]:
            subfilter_list7[randint(0,len(subfilter_list7)-1)].click()
            time.sleep(2)
            filter_done[6].click()















