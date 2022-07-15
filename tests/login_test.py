
from selenium import webdriver
from pages.home_page.login_page import LoginPage
#import unittest
from pages import constants as constants
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        endpoint = "login"
        url = constants.baseUrl + endpoint
        driver.get(url)
        login = LoginPage(driver)
        login.enterEmail(constants.email)
        login.enterPassword(constants.pasword)
        login.loginButton()
        title = driver.title
        assert title == "My Courses"
        driver.get_screenshot_as_file("/Users/apparaojajimoggala/PycharmProjects/pythonSelenium/screenshots/screen.png")
