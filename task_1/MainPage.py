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

    def __init__(self, locator, driver):
        self.locator = locator
        self.driver = driver

    def unique_find_element(self, browser):    
        browser.find_element(self.locator)        
    def enter_word(self, browser, word):
        browser.find_element(self.locator).sent_keys(word)

class LandingHelper():

    Locator_sign_in = (By.ID, "LoginLink")

    def button_signin_is_findable(self,browser):

        button_signin = browser.find_element(self.Locator_sign_in)

        return bool(button_signin)
    
class LoginHelper(BasePage):

    locator_username = (By.CSS_SELECTOR, "#uid")
    licator_password = (By.ID,"passw")

    def find_unique_element(self, browser):

        browser.find_element(self.locator_username)
  
    def enter_word_1(self, word):
        search_field_username = self.unique_find_element(self.locator_username)
        search_field_username.enter_word 
        return search_field_username  #search_field_username = self.find_element(TestfireLocators.Locator_Username)


    def enter_word_2(self,word):

        search_field_password = self.unique_find_element(self.licator_password)

        search_field_password.click()

        search_field_password.send_keys(word)

        return search_field_password

    def click_on_the_search_button(self):

        return self.find_element(TestfireLocators.Locator_button_login,time=2).click()



class UserHelper (Browser):

    

    def find_element(self):

       search_field = self.find_element(TestfireLocators.Locator_button_GO)

       search_field.is_displayed()