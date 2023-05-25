from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BrowserPage:



  def __init__(self, driver): #открывает страницу по URL

    self.driver = driver
    self.base_url = "http://testfire.net"

  def find_element(self, locator,time=5): #ищет один кликабельный элемент и возвращает его
   return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")
  
  def go_back(self):#нажатие на кнопку НАЗАД в браузере

        self.driver.back()

        self.wait_page_loaded()

  def refresh(self):#обновление страницы

        self.driver.refresh()
  
  def go_to_site(self):#переходит по базовому url
        return self.driver.get("http://testfire.net")
  
  