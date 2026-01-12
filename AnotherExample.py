import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context2 = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(5000)

    page2 = context.new_page()  # for new tab, we use same context and new page

    page2.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    page2.wait_for_timeout(5000)
    expect(page2.locator(".orangehrm-upgrade-link")).to_be_visible()

    page3 = context2.new_page()  # this is a new incognitor window, by opening a new context
    # hence it will ask for credentials as we wun this
    page3.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    page3.wait_for_timeout(5000)
    expect(page3.locator(".orangehrm-upgrade-link")).to_be_visible()
    
    
    #page3.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    # page3.wait_for_timeout(10000)
    # expect(page3.locator("//h5[text()='Employee Information']")).to_be_visible()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
