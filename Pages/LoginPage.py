from Config.config import TestData
from Pages.BasePage import BasePage
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://fm.awi.am/page/story')
        time.sleep(20)
        self.driver.maximize_window()
        time.sleep(2)
    def story_title(self):
        get_title = self.driver.title
        print(get_title)
        assert get_title == "The Story - Franck Muller USA"
        story_items = self.driver.find_elements(By.CSS_SELECTOR,".story")
        story_titles = self.driver.find_elements(By.CSS_SELECTOR,".story__title")
        assert story_titles[0].text == "Franck Muller"
        assert story_titles[1].text == "Watchland"
        assert story_titles[2].text == "World Premieres"
        assert story_titles[3].text == "Unique Design"
        assert story_titles[4].text == "WPHH"
        assert story_titles[5].text == "Master of Complications"
        assert story_titles[6].text == "Noble Art"
        print(len(story_titles))
        assert len(story_titles) == 7
    def story_learn_more0(self):
        learn_more_buttons = self.driver.find_elements(By.CSS_SELECTOR,".story__button.button")
        learn_more_buttons[0].click()
        blog_titles = self.driver.find_elements(By.CSS_SELECTOR,".blog__title")  ########### BUG ##########
        assert blog_titles[0].text == "Watchland"
        assert blog_titles[1].text == "World Premieres"
        assert blog_titles[2].text == "Unique Design"
        assert blog_titles[3].text == "WPHH"
        assert blog_titles[4].text == "Master of Complications"
        assert blog_titles[5].text == "Noble Art"

    def story_learn_more1(self):
        story_page = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/a/span")
        story_page.click()
        learn_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".story__button.button")
        learn_more_buttons[1].click()
        blog_titles = self.driver.find_elements(By.CSS_SELECTOR, ".blog__title")
        assert blog_titles[0].text == "story.franckmuller"                                              ###########  BUG  ###########
        assert blog_titles[1].text == "World Premieres"
        assert blog_titles[2].text == "Unique Design"
        assert blog_titles[3].text == "WPHH"
        assert blog_titles[4].text == "Master of Complications"
        assert blog_titles[5].text == "Noble Art"

    def story_learn_more2(self):
        story_page = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/a/span")
        story_page.click()
        learn_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".story__button.button")
        learn_more_buttons[2].click()
        blog_titles = self.driver.find_elements(By.CSS_SELECTOR, ".blog__title")
        assert blog_titles[0].text == "Franck Muller"
        assert blog_titles[1].text == "Watchland"
        assert blog_titles[2].text == "Unique Design"
        assert blog_titles[3].text == "WPHH"
        assert blog_titles[4].text == "Master of Complications"
        assert blog_titles[5].text == "Noble Art"

    def story_learn_more3(self):
        story_page = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/a/span")
        story_page.click()
        learn_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".story__button.button")
        learn_more_buttons[3].click()
        blog_titles = self.driver.find_elements(By.CSS_SELECTOR, ".blog__title")
        assert blog_titles[0].text == "Franck Muller"
        assert blog_titles[1].text == "Watchland"
        assert blog_titles[2].text == "World Premieres"
        assert blog_titles[3].text == "WPHH"
        assert blog_titles[4].text == "Master of Complications"
        assert blog_titles[5].text == "Noble Art"

    def story_learn_more4(self):
        story_page = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/a/span")
        story_page.click()
        learn_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".story__button.button")
        learn_more_buttons[4].click()
        blog_titles = self.driver.find_elements(By.CSS_SELECTOR, ".blog__title")   ######### BUG NO TEXT ###########
        assert blog_titles[0].text == "Franck Muller"
        assert blog_titles[1].text == "Watchland"
        assert blog_titles[2].text == "World Premieres"
        assert blog_titles[3].text == "Unique Design"
        assert blog_titles[4].text == "Master of Complications"
        assert blog_titles[5].text == "Noble Art"

    def story_learn_more5(self):
        story_page = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/a/span")
        story_page.click()
        learn_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".story__button.button")
        learn_more_buttons[5].click()
        blog_titles = self.driver.find_elements(By.CSS_SELECTOR, ".blog__title")
        assert blog_titles[0].text == "Franck Muller"
        assert blog_titles[1].text == "Watchland"
        assert blog_titles[2].text == "World Premieres"
        assert blog_titles[3].text == "Unique Design"
        assert blog_titles[4].text == "WPHH"
        assert blog_titles[5].text == "Noble Art"

    def story_learn_more6(self):
        story_page = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/a/span")
        story_page.click()
        learn_more_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".story__button.button")
        learn_more_buttons[6].click()
        blog_titles = self.driver.find_elements(By.CSS_SELECTOR, ".blog__title")
        assert blog_titles[0].text == "Franck Muller"
        assert blog_titles[1].text == "Watchland"
        assert blog_titles[2].text == "World Premieres"
        assert blog_titles[3].text == "Unique Design"
        assert blog_titles[4].text == "WPHH"
        assert blog_titles[5].text == "Master of Complications"






