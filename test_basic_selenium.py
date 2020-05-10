import pytest
import os
from selenium import webdriver


TEST_APP_URL = "https://www.saucedemo.com"

@pytest.fixture
def browser(request):
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

    driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=caps)
    driver.get(TEST_APP_URL)
    yield driver

    driver.quit()

def test_title(browser):
    assert "Swag Labs" in browser.title

def test_error(browser):
    browser.find_element_by_css_selector(".btn_action").click()

    assert browser.find_element_by_css_selector(".error-button").is_displayed()

def test_login(browser):
    browser.find_element_by_css_selector("#user-name").send_keys("standard_user")
    browser.find_element_by_css_selector("#password").send_keys("secret_sauce")
    browser.find_element_by_css_selector(".btn_action").click()

    assert browser.find_element_by_css_selector(".shopping_cart_container").is_displayed()
