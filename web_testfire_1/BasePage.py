from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import browser

class Baselanding:
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://testfire.net"
    def 
    
    
    
    
    
    wait=WebDriverWait(browser,5)
    url_browser=wait.until(EC.url_to_be("http://testfire.net"))
    #ожидание проверки текщего url
    element_landing=wait.until(EC.element_to_be_clickable(locator))
    #уникальный элемент на странице лендинга - ссылка над картинкой кликабельна
   
    




#driver.find_element(By.CSS_SELECTOR, "#LoginLink > font:nth-child(1)").click()
    #driver.find_element(By.CSS_SELECTOR, "#uid").send_keys("jsmith")
    #driver.find_element(By.CSS_SELECTOR, "#passw").send_keys("demo1234")
    #driver.find_element(By.XPATH, "//input[@value='Login']").click()
    #driver.find_element(By.XPATH, "//input[@value='   GO   ']").is_displayed()
    #driver.close()




    