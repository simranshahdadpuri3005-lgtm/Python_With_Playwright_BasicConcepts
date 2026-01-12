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

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


#we can use PWDEBUG=1 to use the playwright debugger and see where the steps are failing
# we can use the line by line execution in the new window that opens
# we can use the step over button to go to the next button

# to come out of debug mode , we need to excute console command as PWDEBUG=0
# we can use page.pause() as a breakpoint after any line of execution while debugging




