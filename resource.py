from selenium import webdriver
import os
from robot.api.deco import keyword


TEST_APP_URL = "https://www.saucedemo.com"
driver = {}

class SauceDemo(object):

    def __init__(self):
        self.driver = {}

    @keyword
    def start_session(self):
        caps = {
            "browserName": "Chrome",
            "sauce:options": {
                "browserName": "Chrome",
                "platformName": "Windows 10",
                "browserVersion": "latest"
            }
        }

        username = os.environ['SAUCE_USERNAME']
        access_key = os.environ['SAUCE_ACCESS_KEY']

        remote_url = 'https://{}:{}@ondemand.saucelabs.com/wd/hub/'.format(username, access_key)

        self.driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=caps)

    @keyword
    def open_login_page(self):
        self.driver.get(TEST_APP_URL)

    @keyword
    def title_is_correct(self):
        assert "Swag" in self.driver.title

    @keyword
    def page_should_contain_error(self):
        assert self.driver.find_element_by_css_selector(".error-button").is_displayed()

    @keyword
    def login_as_user(self, username, password):
        self.driver.find_element_by_css_selector("#user-name").send_keys(username)
        self.driver.find_element_by_css_selector("#password").send_keys(password)
        self.driver.find_element_by_css_selector(".btn_action").click()

    @keyword
    def should_be_on_inventory_page(self):
        assert self.driver.find_element_by_css_selector(".shopping_cart_container").is_displayed()

    @keyword
    def end_session(self):
        self.driver.quit()
