from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def test_login():
    global driver
    driver = webdriver.Firefox() #executable_path="D:\\python\\DATA SCIENCE\\edgedriver.exe"
    driver.implicitly_wait(10)
    driver.maximize_window()
def test_setup(test_login):
    driver.get('http://testfire.net')
    driver.find_element(By.CSS_SELECTOR, "#LoginLink > font:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#uid").send_keys("jsmith")
    driver.find_element(By.CSS_SELECTOR, "#passw").send_keys("demo1234")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    driver.find_element(By.CSS_SELECTOR, "#LoginLink > font:nth-child(1)").click()
    driver.back()
    url = "http://testfire.net/login.jsp" #ОР
    #url = "http://testfire.net/bank/main.jsp" ФР
    assert url == driver.current_url
    driver.close()
