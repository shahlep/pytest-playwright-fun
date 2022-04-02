import os
from playwright.sync_api import Playwright, sync_playwright, expect
from pytest import mark

from home_page_elements import HomePage

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config

    PASSWORD = utils.secret_config.PASSWORD


@mark.ui
def test_homepage_navigation(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    page.goto(HomePage.home_url)
    page.pause()

    page.locator(HomePage.login_password_input).click()

    page.locator(HomePage.login_password_input).fill(PASSWORD)

    page.locator(HomePage.login_submit).click()

    page.wait_for_load_state()
    #expect(page).to_have_url(HomePage.home_url)

    page.locator(HomePage.navbar_catalog_btn).click()

    expect(page).to_have_url(HomePage.catalog_url)

    page.locator(HomePage.navbar_contact_btn).click()

    expect(page).to_have_url(HomePage.contact_url)

    page.locator(HomePage.header_btn).click()

    expect(page).to_have_url(HomePage.home_url)

    context.close()
    browser.close()
