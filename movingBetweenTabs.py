#playwright codegen --target python https://practicetestautomation.com/practice-test-login/
# It is liking generating the code by just doing the actions. we need not write the code. you perform the actions and the code is written automatically

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()

 # Open Courses
    page.locator("//a[text()='Courses']").click()

  # ---------- FIRST NEW TAB ----------
    with page.expect_popup() as page1_newTab:  #all properties of new tab will be stored in page1_NewTab
        page.get_by_role("link", name="Selenium WebDriver: Selenium Automation Testing with Java").click()
   
    page1 = page1_newTab.value
    page1.wait_for_load_state()
    expect(page1.locator("//h1[text()='Selenium WebDriver: Selenium Automation Testing with Java']")).to_be_visible(timeout=60000)

 # ---------- SECOND NEW TAB ----------
    with page.expect_popup() as page2_anotherTab:
            page.get_by_role("link", name="Selenium WebDriver: Selenium Automation Testing with Python").click()

    page2 = page2_anotherTab.value
    page1.wait_for_load_state()
    expect(page2.locator("//h1[text()='Selenium WebDriver: Selenium Automation Testing with Python']")).to_be_visible(timeout=60000)
   
   
   
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)




