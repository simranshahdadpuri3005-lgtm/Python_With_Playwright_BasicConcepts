from playwright.sync_api import sync_playwright, expect

def launchPracticeWebsite(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")  #navigate to page
    page.wait_for_load_state("networkidle", timeout=60000) # it will make sure that no more loading is happening
    expect(page).to_have_title("Test Login | Practice Test Automation") #validate the page title

def validateVisibilityOfElement(locatorVariable):
    expect(locatorVariable).to_be_visible()  

def loginToWebsite(page, usernameValue, passwordValue):
    usernameTextbox = page.locator("input#username")
    passwordTextbox = page.locator("input#password")

    usernameTextbox.fill(usernameValue)
    passwordTextbox.fill(passwordValue)

    submitBtn = page.locator("button#submit")
    submitBtn.click()
    page.wait_for_load_state("networkidle", timeout=60000)
    expect(page).to_have_title("Logged In Successfully | Practice Test Automation")


def validatePositiveScenario():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        launchPracticeWebsite(page)
        
        testLoginText = page.locator("//h2[text()='Test login']")
        validateVisibilityOfElement(testLoginText)
        usernameTextbox = page.locator("input#username")  #check it the username textbox is visible or not. locator format is (tagname#id)
        #expect(usernameTextbox).to_be_visible()
        validateVisibilityOfElement(usernameTextbox)
        passwordTextbox = page.locator("input#password")  #check if the password textbox is visible or not
        validateVisibilityOfElement(passwordTextbox)

        loginToWebsite(page,"student", "Password123")

#testcase 2- incorrect username
def validateNegativeScenarioWithInvalidUsername():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        launchPracticeWebsite(page)
        
        testLoginText = page.locator("//h2[text()='Test login']")
        validateVisibilityOfElement(testLoginText)
        usernameTextbox = page.locator("input#username")  
        validateVisibilityOfElement(usernameTextbox)
        passwordTextbox = page.locator("input#password")
        validateVisibilityOfElement(passwordTextbox)

        loginToWebsite(page, "student222", "Password123")

validatePositiveScenario()
validateNegativeScenarioWithInvalidUsername()

    




