#Playwright can open web applications but cannot open Desktop applications

from playwright.sync_api import sync_playwright

with sync_playwright() as p:   
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.amazon.in/")

    #page.locator("Xpath") - format
    #page.get_by_placeholder("Search Amazon.in").fill("iPhone")
    page.get_by_role("searchbox").fill("iPhone")
   
    page.wait_for_timeout(5000)
    browser.close()

with sync_playwright() as q:   
    browser = q.chromium.launch(headless=False)
    #browser = q.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto("https://bootswatch.com/")

    #page.get_by_label("Toggle theme").first.click()
    page.get_by_label("Toggle theme").nth(1).click()
    page.wait_for_timeout(5000)
    browser.close()
 
    #there are multiple get_by locators, just try
    
