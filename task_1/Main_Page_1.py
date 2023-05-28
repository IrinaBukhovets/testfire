from Browser import Browser
from selenium.webdriver.common.by import By

class TestfireLocators:

    Locator_sign_in = (By.ID, "LoginLink")
    Locator_Username = (By.CSS_SELECTOR, "#uid")
    Locator_Password = (By.ID,"passw")
    Locator_button_login = (By.XPATH,"//[@input[@value='Login']")
    Locator_button_GO = (By.XPATH,"//input[@value='   GO   ']")

class LoginHelper(Browser):
    def enter_word (self,word):
        enter_word_username = self.find_element(TestfireLocators.Locator_Username)
        enter_word_username.click()
        enter_word_username.send_keys(word)
        return enter_word_username

