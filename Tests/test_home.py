from Pages.Homepage import Homepage


class TestHome:
    def test_homepage_tags(self,setup):
        hp= Homepage(self.driver)
        hp.click_tags_one_by_one()
        child_window= self.driver.window_handles[0]
        self.driver.switch_to.window(child_window)
        assert "method-overriding-in-python" in self.driver.current_url