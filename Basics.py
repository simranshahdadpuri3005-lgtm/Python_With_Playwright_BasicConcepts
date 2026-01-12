#Playwright can open web applications but cannot open Desktop applications

from playwright.sync_api import sync_playwright
#playwright is library, sync_api is the pacakge and sync_playwright is the function

#p = sync_playwright().start()  #initializing the playwright and storing it in variable
with sync_playwright() as p:    # another and most used way of initiatlizing the playwright

    browser = p.chromium.launch(headless=False)  #launch the chromium browser
    #browser = p.chromium.launch(channel='msedge', headless=False)  #launch the cedge browser this way also using the channel
    #headless = false means the user want to see the actions on UI, else it will run in the background only and the user cannot see anything

    page = browser.new_page()
    page.goto("https://www.amazon.in/")
    #page.close()
    browser.close()
    #p.stop()  

    #when we use the with block, we need not explicitly stop the playwright, it will automatically close and also it will not use any of the memory in background
    #with block automatically provides the stopping, cleans the code after the execution, close the browser also
    #we can use Ctrl + click to see the position as to where the variable is initiatlized