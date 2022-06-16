import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--url",action="store", default="https://www.thedigitalcatonline.com/blog/2014/05/19/method-overriding-in-python/"
    )

@pytest.fixture
def setup(request):
    browser_name= request.config.getoption("browser_name")
    options =Options()
    options.add_argument("--start-maximized")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=options)
    elif browser_name ==  "firefox" or "FF":
        driver= webdriver.Firefox(GeckoDriverManager().Install())
    else:
        print("No driver")
    url= request.config.getoption("url")
    driver.get(url)
    request.cls.driver= driver

    yield
    # driver.close()


