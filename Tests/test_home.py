import pytest

from Pages.Homepage import Homepage
from Utilities.customLogger import LogGen
from Utilities.readConfig import ReadConfig


class TestHome:
    logger = LogGen.loggen()
    @pytest.fixture
    def class_setup(self):
        self.hp = Homepage(self.driver)


    #method was written for another website.Kept here just for information purpose
    def test_homepage_tags(self,setup,class_setup):
        self.logger.info("***********TC_test_homepage_tags **********")
        self.logger.info("***********Click on tags **********")
        self.hp.click_tags_one_by_one()
        child_window= self.driver.window_handles[0]
        self.driver.switch_to.window(child_window)
        if "method-overriding-in-python" in self.driver.current_url:
            assert True
            self.logger.info("***********Test Case Passed **********")
        else:
            self.logger.error("***********Test case failed**********")

    def test_login(self,setup,class_setup):
        self.logger.info("***********TC_test_login **********")
        self.logger.info("*********** Verify Login **********")
        self.hp.login(ReadConfig.getUsername(),ReadConfig.getPassword())
        if "dashboard" in self.driver.current_url:
            assert  True
            self.logger.info("**********Login Test Passed**********")

    def test_login1(self,setup,class_setup):
        self.logger.info("***********TC_test_login **********")
        self.logger.info("*********** Verify Login **********")
        self.hp.login(ReadConfig.getUsername(),ReadConfig.getPassword())
        if "dashboard" in self.driver.current_url:
            assert  True
            self.logger.info("**********Login Test Passed**********")

    def test_login2(self,setup,class_setup):
        self.logger.info("***********TC_test_login **********")
        self.logger.info("*********** Verify Login **********")
        self.hp.login(ReadConfig.getUsername(),ReadConfig.getPassword())
        if "dashboarddd" in self.driver.current_url:
            assert  True
            self.logger.info("**********Login Test Passed**********")

