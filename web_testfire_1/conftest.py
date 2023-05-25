from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="session") #Это означает что данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию

def browser():
 driver = webdriver.Firefox()
 #driver = webdriver.Edge(executable_path="C:\\Users\\User\\Desktop\\msedgedriver.exe")
 yield driver #yield разделяет функцию на часть — до тестов и после тестов.
 driver.quit() #функцию quit-завершает сессию и убивает экземпляр webdriver.

