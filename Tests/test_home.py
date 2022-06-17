import pytest

from Pages.Homepage import Homepage


class TestHome:
    @pytest.fixture
    def class_setup(self):
        self.hp = Homepage(self.driver)

    @pytest.mark.xfail
    #method was written for another website.Kept here just for information purpose
    def test_homepage_tags(self,setup):
        self.hp.click_tags_one_by_one()
        child_window= self.driver.window_handles[0]
        self.driver.switch_to.window(child_window)
        assert "method-overriding-in-python" in self.driver.current_url

    def test_login(self,setup,class_setup):
        self.hp.login("Admin","admin123")
        assert "dashboard" in self.driver.current_url


