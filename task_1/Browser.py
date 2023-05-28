from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self, driver): #открывает страницу по URL
        self.driver = driver
        self.base_url = "http://testfire.net/login.jsp"
    
    def find_element(self,locator,time=5): #ищет один кликабельный элемент и возвращает его  
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def go_back(self):#нажатие на кнопку НАЗАД в браузере
        self.driver.back()

    def refresh(self):#обновление страницы
        self.driver.refresh()

    def go_to_site(self):#переходит по базовому url
        self.driver.get(self.base_url)
    