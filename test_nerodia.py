import pytest
import os
from selenium import webdriver
from nerodia.browser import Browser


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

    remote = webdriver.Remote(command_executor=remote_url, desired_capabilities=caps)
    driver = Browser(browser=remote, desired_capabilities=caps)
    driver.goto(TEST_APP_URL)
    yield driver

    driver.quit()

def test_title(browser):
    assert "Swag Labs" in browser.title

def test_error(browser):
    browser.text_field(className="btn_action").click()

    assert browser.button(".error-button").is_displayed()

def test_login(browser):
    browser.text_field(id="user-name").send_keys("standard_user")
    browser.text_field(id="password").send_keys("secret_sauce")
    browser.button(className="btn_action").click()

    assert browser.element(".shopping_cart_container").is_displayed()
