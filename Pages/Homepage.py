from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Base.BaseClass import BaseClass


class Homepage(BaseClass):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver

    tags = (By.XPATH,"//div[@class='post-info']/p[@class='tags']/a")
    user= (By.XPATH,"//input[@name='txtUsername']")
    pwd = (By.XPATH,"//input[@name='txtPassword']")
    login_button= (By.XPATH,"//input[@name='Submit']")

    def click_tags_one_by_one(self):
        tag_elements= self.driver.find_elements(*Homepage.tags)
        act=  ActionChains(self.driver)
        print(len(tag_elements))
        for tag in tag_elements:
            act.key_down(Keys.CONTROL).click(tag).perform()
            print(tag.text)

    def login(self,uname,password):
        self.driver.find_element(*Homepage.user).send_keys(uname)
        self.driver.find_element(*Homepage.pwd).send_keys(password)
        self.driver.find_element(*Homepage.login_button).click()
