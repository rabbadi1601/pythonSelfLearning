import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
element= driver.find_element(By.NAME,"search")
# set implicit wait time
driver.implicitly_wait(10) # seconds

print( "  before js call ")
# java script to highlight the element
driver.execute_script("arguments[0].style.border='3px solid red'",element)
print( "  AFTER js call ")
time.sleep(10)
driver.close()

