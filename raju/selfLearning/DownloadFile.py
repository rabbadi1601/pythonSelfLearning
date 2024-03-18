import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
full_path = os.getcwd()
print(Path(full_path).parents[0])
os.chdir(Path(full_path).parents[0])
os.chdir("configurations")
desired_path = os.getcwd()
print("111 "+full_path)
chromeOptions = webdriver.ChromeOptions()
#prefs = {"download.default_directory": "/Users/rabbadi/Documents/python3_api_testing_Feb162024/pythonSelfLearning"}
prefs = {"download.default_directory": desired_path}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chromeOptions)

driver.maximize_window()

driver.get("http://omayo.blogspot.com/p/page7.html")
driver.find_element(By.LINK_TEXT,"ZIP file").click()
#driver.find_element_by_link_text("ZIP file").click()