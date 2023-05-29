from Browser import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestfireLocators:
    
    Locator_sign_in = (By.ID, "LoginLink")
    Locator_Username = (By.ID,"uid")
    Locator_Password = (By.ID,"passw")
    Locator_button_login = (By.XPATH,"//[@input[@value='Login']")
    Locator_button_GO = (By.XPATH,"//input[@value='   GO   ']")

class BasePage:

    def __init__(self, locator):
        self.locator = locator   

    def unique_find_element(self, browser):
        browser = Browser()   
        browser.find_element(self.locator)        

    def enter_word(self, word):
        Browser().find_element(self.locator).send_keys(word)

    def click_on_the_button(self, browser):
        browser = Browser()   
        browser.find_element(self.locator).click()

    def element_is_displayed(self,browser):
        browser = Browser()
        browser.find_element(self.locator).is_displayed()

class LandingHelper(BasePage):
    
    locator_sign_in = (By.ID, "LoginLink")

    def __init__(self):
        super().__init__(locator=self.locator_sign_in)
    
    def button_signin_click(self):
       self.click_on_the_button(browser = Browser())

class LoginHelper1(BasePage):

    locator_username = (By.CSS_SELECTOR, "#uid")

    def __init__(self):
        super().__init__(locator=self.locator_username)

    def enter_login(self, login):
        self.enter_word(word=login)

class LoginHelper2(BasePage):

    licator_password = (By.ID,"passw")

    def __init__(self):
        super().__init__(locator=self.licator_password)    

    def enter_password(self, password):
        self.enter_word(word=password)

class LoginHelper3(BasePage):

    locator_button_login = (By.XPATH, "//input[@value='Login']")

    def __init__(self):
        super().__init__(locator=self.locator_button_login)

    def click_on_the_button_login(self):
        self.click_on_the_button(browser=Browser())

    def button_login_on_the_page(self):
        self.element_is_displayed(browser=Browser())

class UserHelper (BasePage):

    locator_button_GO = (By.XPATH,"//input[@value='   GO   ']")

    def __init__(self):
        super().__init__(locator=self.locator_button_GO)

    def button_GO_on_the_page(self):
        self.element_is_displayed(browser=Browser())