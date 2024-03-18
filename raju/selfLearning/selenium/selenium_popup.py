import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.maximize_window()
# https://the-internet.herokuapp.com/basic_auth this url will show the pop and we are not able to find the locators for username and password
# so we will pass the username and password in the url like below , here user name and password are admin/admin
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
print(driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations')]").text)
assert driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations')]").text.__contains__('Congratulations!')
time.sleep(3)
driver.close()

WebDriverWait