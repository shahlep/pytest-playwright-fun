import os

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pytest import mark

from home_page_elements import HomePage


@mark.ui
def test_homepage_navigation(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://shahlep.myshopify.com/password
    #page.goto("https://shahlep.myshopify.com/password")
    page.goto(HomePage.home_url)
    page.pause()
    # Click input[name="password"]
    page.locator(HomePage.login_password_input).click()
    # Fill input[name="password"]
    page.locator(HomePage.login_password_input).fill(os.environ['PASSWORD'])
    # Click button:has-text("Enter")
    page.locator(HomePage.login_submit).click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/")
    #expect(page).to_have_url(HomePage.home_url)
    # Click span:has-text("Catalog")
    page.locator(HomePage.navbar_catalog_btn).is_visible(timeout=5000)
    page.locator(HomePage.navbar_catalog_btn).click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/collections/all")
    expect(page).to_have_url(HomePage.catalog_url)
    # Click span:has-text("Home")
    page.locator(HomePage.navbar_home_btn).is_visible(timeout=5000)
    page.locator(HomePage.navbar_home_btn).click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/")
    expect(page).to_have_url(HomePage.home_url)

    # Click span:has-text("Contact")
    page.locator(HomePage.navbar_contact_btn).is_visible(timeout=5000)
    page.locator(HomePage.navbar_contact_btn).click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/pages/contact")
    expect(page).to_have_url(HomePage.contact_url)
    # Click span:has-text("shahlep")
    page.locator(HomePage.header_btn).is_visible(timeout=5000)
    page.locator(HomePage.header_btn).click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/")
    expect(page).to_have_url(HomePage.home_url)

    # ---------------------
    context.close()
    browser.close()
