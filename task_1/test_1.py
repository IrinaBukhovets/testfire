from MainPage import LandingHelper
from Main_Page_1 import LoginHelper
from MainPage import UserHelper
from selenium import webdriver



def test_login (browser):

    #browser.go_to_site()

    #landing_page = LandingHelper()

    #assert landing_page.button_signin_is_findable(browser=browser)

    login_page_username = LoginHelper(browser)

    browser.go_to_site()

    login_page_username.enter_word("jsmith")


