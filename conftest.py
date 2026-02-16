import pytest

from pages.login_page import LoginPage
from utilities import test_data


@pytest.fixture
def setup_login(page):
    login_page =LoginPage(page)
    login_page.navigate_to()
    login_page.login(test_data.credentials["valid_username"],
                     test_data.credentials["valid_password"])

    yield page

