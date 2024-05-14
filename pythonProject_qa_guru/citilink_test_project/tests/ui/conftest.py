import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def settings_browser():
    browser.config.base_url = "https://www.citilink.ru/login//"
    browser.config.timeout = 6.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()