from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Base.BaseClass import BaseClass


class Homepage(BaseClass):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver

    tags = (By.XPATH,"//div[@class='post-info']/p[@class='tags']/a")

    def click_tags_one_by_one(self):
        tag_elements= self.driver.find_elements(*Homepage.tags)
        act=  ActionChains(self.driver)
        print(len(tag_elements))
        for tag in tag_elements:
            act.key_down(Keys.CONTROL).click(tag).perform()
            print(tag.text)
