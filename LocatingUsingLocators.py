
from playwright.sync_api import sync_playwright, expect
import re  
# re is used for regular expression

# with sync_playwright() as p:   
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.hyrtutorials.com/p/add-padding-to-containers.html")

     
    #we have 2 types of locators - xpaths and Css
    # xpath syntax  :
    # //tagname[@attribute='value']
    # 2 types of xpath - relative  and absolute - if we start with 2 slashes //, it is relative xpath. it starts from anywhere in the page
    # absolute xpath -it will start with single slash ,  it starts from the top of the page, we have to start from root node

    #  indexing helps to identify unique elements when the xpath turns more than one matches
    # example : (//input[@name='name'])[1] - 1 is the index here

    #to get immediate following sibling
    # (//input[@name='name'])[1]/following-sibling::label[1]

    #(//input[@name='name'])[1]/preceding-sibling::label

    # //label[text()='Last Name']

    # //label[text()='First Name ']/following-sibling::label[1]

    # //label[text()='Last Name']//preceding-sibling::input

    # //label[text()='Last Name']//preceding-sibling::input[@name='name']

    #going from parent to desired node

    # //div[@id='Postwidegt1']/div/h2

    # //div[@id='Postwidegt1']//h2

    #for the first child add single slash, for all the children inside children use //

    # //div[@id='sidebar(1)']/div[@id='HTML2']

    # //div[@id='HTML4']/parent::div

    #//div[@id='HTML4']/ancestor::div

    # //label[contains(text(),'Last')]

    # //*[contains(text(),'Last')]  it means any tag name that contains text as 'Last'

    # //tagname[contains(@atrribute, 'value')]

    # CSS formats
    # tagname[attribute=' value']   
    #no double slash here


    # we can locate the class using the regular way of tagname as above or by using the . (dot) symbol
    # for example 
    # <in the DOMS we can see as <i class="hm-icon nav-sprite"> or i.hm-icon.nav-sprite(tagname.value)
    
    # we can locate it using i[@class = 'hm-icon nav-sprite'] of .hm-icon.nav-sprite  (we have replaced the space between hm-icon and nav-sprite with another .)

    # for the id locator we can use the # (hash) symbol
    # <a id="hm-hamburger"> or #hm-hamburger or a#hm-hamburger (tagname#value)
    
    # only for class and id attributes we have these shortcuts
    # if we give #desktop-banner div then it will collect all the children and grandchildren of element with id as desktop-banner
    # if we give #desktop-banner>div then it will collect thr first child of element with id as desktop-banner
    #
    # with css we can traverse only towards child and not to the parent


    # page.wait_for_timeout(5000)
    # browser.close()

def clickFemaleRadioBtn():
    femaleRadioBtn = page.locator("#female")
    femaleRadioBtn.click()

def checkAutomationCheckbox():
    automationChkbox = page.locator(".Automation")
    automationChkbox.check()
    page.wait_for_timeout(3000)
    automationChkbox.uncheck()

def selectDropdownValue(variableselection):
    dropDownPath = page.locator("#testingDropdown")
    dropDownPath.select_option(variableselection)


with sync_playwright() as p:   
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto("https://www.artoftesting.com/samplesiteforselenium/")

    expect(page).to_have_title("Sample Webpage for Selenium Automation Practice | ArtOfTesting")
    #expect is used for assertion

    expect(page).to_have_title(re.compile("Sample Webpage for Selenium Automation Practice | ArtOfTesting"))
    #re.compile works similar to contains function 

    pageTitle = page.title()
    print("the title of opened page is ", pageTitle)

    assert pageTitle == "Sample Webpage for Selenium Automation Practice | ArtOfTesting"

    if pageTitle == "Sample Webpage for Selenium Automation Practice | ArtOfTesting":
        print("matched")
    else:
        print("not matched")

    expect(page.locator("//a[text()='This is a link']")).to_be_visible()

    #another way to write above command
    linkElement = page.locator("//a[text()='This is a link']")
    expect(linkElement).to_be_visible

    linkElement.click()
    expect(page.locator("#fname")).to_be_visible()
    page.locator("#fname").scroll_into_view_if_needed()
    # to enter the data in textbox, we can use fill() or type() functions
    page.locator("#fname").clear   #we are clearing the textbox data, if any is present already, using clear command, so that the new data is not appended
    page.locator("#fname").fill("testname")
    
    #page.locator("#fname").clear   #we are clearing the textbox data, if any is present already, using clear command, so that the new data is not appended
    #page.locator("#fname").type("testname", delay=1)

    #in the type we can also give the delay while entering each character
    
    clickFemaleRadioBtn()
    checkAutomationCheckbox()
    selectDropdownValue('Performance Testing')
    page.wait_for_timeout(2000)
    selectDropdownValue('Automation')


    page.reload()   #refreshing the screen
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
   
    page.wait_for_load_state("networkidle")  #wait until the page is completely loaded
    
    selectDropdownValue('Automation')
    page.locator("#fname").wait_for(state='visible')  #wait until the locator element given, first name in this case, is visible

    pageUrl = page.url  #url is not a function and hence we should not give brackets
    print(pageUrl)

    pageContent = page.content() #content will give the full page content that can be seen in Doms
    #print(pageContent)

    linkTextBtn = page.locator("//div[@id='commonWebElements']/p/a").inner_text()  #innertext will give the text of the locator's element
    print(linkTextBtn)

    page.wait_for_timeout(5000)
    browser.close()

    #assert and expect are hard validations






    
