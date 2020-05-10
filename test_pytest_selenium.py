import pytest


TEST_APP_URL = "https://www.saucedemo.com"

@pytest.fixture
def browser(selenium):
    selenium.get(TEST_APP_URL)
    yield selenium


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
