from typing import Generator
import pytest
from playwright.async_api import Page
from playwright.sync_api import Playwright, sync_playwright
from credentials import _user_name, _user_password


class PlaywrightPage:


    @pytest.fixture(scope="session")
    def playwright(self) -> Generator[Playwright, None, None]:
        with sync_playwright() as p:
            yield p

    @pytest.fixture(scope="function")
    def page(self, playwright: Playwright) -> Generator[Page, None, None]:
        browser = playwright.chromium.launch(headless=True, devtools=True, slow_mo=1000)
        context = browser.new_context(locale="en_EN", viewport=None)
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill(_user_name)
        page.locator("#password").fill(_user_password)
        page.locator("#login-button").click()

        yield page

        page.close()
        context.close()
        browser.close()
