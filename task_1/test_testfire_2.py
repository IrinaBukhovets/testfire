import time
from MainPage import LandingHelper
from MainPage import LoginHelper1
from MainPage import LoginHelper2
from MainPage import LoginHelper3
from MainPage import UserHelper
from selenium import webdriver
from Browser import Browser

def test_back (browser):    
    press_sign_in_button = LandingHelper()
    press_sign_in_button.button_signin_click()
    time.sleep(2)
    enter_username = LoginHelper1()
    enter_username.enter_login("jsmith")
    time.sleep(2)
    enter_password = LoginHelper2()
    enter_password.enter_password ("demo1234")
    time.sleep(2)
    press_login_button = LoginHelper3()
    press_login_button.click_on_the_button_login()
    time.sleep(2)
    element_button_GO_is_displayed = UserHelper()
    element_button_GO_is_displayed.button_GO_on_the_page()
    time.sleep(2)
    press_sign_in_button_2 = LandingHelper()
    press_sign_in_button_2.button_signin_click()
    time.sleep(2)
    back_browser = Browser()
    back_browser.go_back()
    time.sleep(2)
    element_button_LOGIN_is_displayed = LoginHelper3()
    element_button_LOGIN_is_displayed.button_login_on_the_page()
    assert element_button_LOGIN_is_displayed