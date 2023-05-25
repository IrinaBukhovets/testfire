from BrowserPage import BrowserPage

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

class TestfireLocators:
 Locator_sign_in = (By. ID, "LoginLink")
 Locator_Username = (By.ID, "uid")
 Locator_Password = (By.ID, "passw")
 Locator_button_login = (By.XPATH, "//[@input[@value='Login']")
 Locator_button_GO = (By.XPATH, "//input[@value='   GO   ']")


class LandingHelper (BrowserPage):

    def click_element_to_be_clickable (self):
      search_field = self.find_element(TestfireLocators.Locator_sign_in)
      search_field.click()
      return search_field

    #нужно еще проверить что появилась кнопка login, т е загрузилась другая страница   

class LoginHelper (BrowserPage):

    def enter_word_1(self, word):
        search_field_username = self.find_element(TestfireLocators.Locator_Username)
        search_field_username.click()
        search_field_username.send_keys(word)
        return search_field_username
    def enter_word_2(self, word):
        search_field_password = self.find_element(TestfireLocators.Locator_Password)
        search_field_password.click()
        search_field_password.send_keys(word)
        return search_field_password
    def click_on_the_search_button(self):
        return self.find_element(TestfireLocators.Locator_button_login,time=2).click()

class UserHelper (BrowserPage):
    
    def find_element(self):
       search_field = self.find_element(TestfireLocators.Locator_button_GO)
       search_field.is_displayed()