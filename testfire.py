from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://testfire.net')

sign_in = driver.find_element(By.CSS_SELECTOR, "#LoginLink > font:nth-child(1)")
sign_in.click()

username = driver.find_element(By.CSS_SELECTOR, "#uid")
username.send_keys("jsmith")
print("Input Username")

password = driver.find_element(By.CSS_SELECTOR, "#passw")
password.send_keys("demo1234")
print("Input Password")

#button_login = driver.find_element(By.CSS_SELECTOR, "#login > table > tbody > tr:nth-child(3) > td:nth-child(2) > input[type=submit]")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
print("Click Login Button")

button_go = driver.find_element(By.XPATH, "//input[@value='   GO   ']")
button_exist = button_go.is_displayed() #присутствует кнопка GO
print(button_exist)

driver.find_element(By.CSS_SELECTOR, "#LoginLink > font:nth-child(1)").click()
driver.back()
url = "http://testfire.net/login.jsp"
assert url == driver.current_url
print("GOOD URL")
#сравнение
#assert 



