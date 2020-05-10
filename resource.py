from selenium import webdriver
import os


TEST_APP_URL = "https://www.saucedemo.com"

class SauceLabs(object):

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

    def open_login_page(self):
        self.driver.get(TEST_APP_URL)
    
    def title_is_correct(self):
        assert "Swag" in self.driver.title

    def page_should_contain_error(self):
        assert self.driver.find_element_by_css_selector(".error-button").is_displayed()

    def login_as(self, username, password):
        self.driver.find_element_by_css_selector("#user-name").send_keys(username)
        self.driver.find_element_by_css_selector("#password").send_keys(password)
        self.driver.find_element_by_css_selector(".btn_action").click()

    def should_be_on_inventory_page(self):
        assert self.driver.find_element_by_css_selector(".shopping_cart_container").is_displayed()

    def end_session(self):
        self.driver.quit()
