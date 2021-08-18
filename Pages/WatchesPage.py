from Config.config import TestData
from Pages.BasePage import BasePage
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WatchesPage(BasePage):
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
