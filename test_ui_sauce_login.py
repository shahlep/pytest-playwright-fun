import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pytest import mark


@mark.sauce
@mark.parametrize("user, password", [('standard_user', 'secret_sauce'),
                                     pytest.param('standard_user', 'secret', marks=mark.xfail),
                                     pytest.param('test', 'secret_sauce',marks=mark.xfail),
                                     pytest.param('standard_user', '',marks=mark.xfail),
                                     pytest.param('', 'secret_sauce',marks=mark.xfail),
                                     pytest.param('', '',marks=mark.xfail)])
def test_login_scenarios(playwright: Playwright, user, password) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    page.goto('https://www.saucedemo.com/')

    page.locator('#user-name').click()
    page.locator('#user-name').fill(user)

    page.locator('#password').click()
    page.locator('#password').fill(password)

    page.locator('#login-button').click()

    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

    context.close()
    browser.close()
