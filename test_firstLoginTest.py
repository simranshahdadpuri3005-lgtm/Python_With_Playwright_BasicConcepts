from playwright.sync_api import Page  # this will help to get the suggestions while writing the code
import pytest

@pytest.mark.order(4)
def test_launchTheURL(page: Page):
    page.goto("https://www.amazon.in/")
    print("4th order")
    page.wait_for_timeout(5000)

@pytest.mark.order(1)
def test_launchTheURL2(page: Page):
    page.goto("https://www.amazon.in/")
    print("1st order")
    page.wait_for_timeout(5000)

@pytest.mark.order(2)
@pytest.mark.skip()
def test_launchTheURL3(page: Page):
    page.goto("https://www.amazon.in/")
    print("2nd order")
    page.wait_for_timeout(5000)

@pytest.mark.order(3)
def test_launchTheURL4(page: Page):
    page.goto("https://www.amazon.in/")
    print("3rd order")
    page.wait_for_timeout(5000)
    
    # pip install pytest-xdist - for parallel exeuction of testcases for pytest
    # pytest --headed -n 10 ---- this will run 10 parallel exeuctions- 10 browsers will open depending on the number of testcases
    #pytest --headed -n 3 --browser firefox    ---- to run in firefox
    #pytest --headed -n 3 --browser firefox  --browser chrromium   ----- the tst cases will be exeucted in chromium and firefox both
    # by default, it will be chromium
    # if we do not give the sequence it will take by alphabetical order of testcase names
    # pip install pytest_dependency - to make sure if one test result is required for another test case execution
    #  
    

