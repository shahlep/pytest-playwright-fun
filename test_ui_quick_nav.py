from playwright.sync_api import Playwright, sync_playwright, expect


def test_website_navigation(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=1000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://shahlep.myshopify.com/password
    page.goto("https://shahlep.myshopify.com/password")

    # Click input[name="password"]
    page.locator("input[name=\"password\"]").click()
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("taisia<3")

    # Click button:has-text("Enter")
    page.locator("button:has-text(\"Enter\")").click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/")
    expect(page).to_have_url("https://shahlep.myshopify.com/")
    #assert page.url()
    # Click span:has-text("Catalog")
    page.locator("span:has-text(\"Catalog\")").click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/collections/all")
    expect(page).to_have_url("https://shahlep.myshopify.com/collections/all")
    # Click span:has-text("Home")
    page.locator("span:has-text(\"Home\")").click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/")
    expect(page).to_have_url("https://shahlep.myshopify.com/")

    # Click span:has-text("Contact")
    page.locator("span:has-text(\"Contact\")").click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/pages/contact")
    expect(page).to_have_url("https://shahlep.myshopify.com/pages/contact")
    # Click span:has-text("shahlep")
    page.locator("span:has-text(\"shahlep\")").click()
    # expect(page).to_have_url("https://shahlep.myshopify.com/")
    expect(page).to_have_url("https://shahlep.myshopify.com/")

    # ---------------------
    context.close()
    browser.close()
