import time

import pytest

from pages.login_page import LoginPage
from utilities import test_data


@pytest.fixture
def open_url(page):
    login_page = LoginPage(page)
    login_page.navigate_to()

    yield  login_page


def test_valid_login(open_url):
    open_url.login(
        test_data.credentials["valid_username"],
        test_data.credentials["valid_password"]
    )
    assert open_url.page.url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(3)


def test_invalid_login(open_url):
    open_url.login(
        test_data.credentials["invalid_username"],
        test_data.credentials["invalid_password"]
    )
    current_alert_message = open_url.get_alert_message()
    expected_alert_message = "Login failed! Please ensure the username and password are valid."

    assert current_alert_message.strip() == expected_alert_message.strip()


    time.sleep(3)


