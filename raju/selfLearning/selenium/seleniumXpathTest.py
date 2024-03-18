from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")

## //XPath Operators
driver.find_element(By.XPATH,"//input[@maxlength=10]").send_keys("Test")
driver.find_element(By.XPATH,"//input[@maxlength!=10]").send_keys("Test2")
testElement=driver.find_elements(By.XPATH,"//input[@maxlength>=10]")

# set implicit wait time
driver.implicitly_wait(10) # seconds


print(type(testElement)) #<class 'list'>
for value in testElement:
 print(value.get_attribute("name"))
 print(value.get_attribute("type"))

print("elements size 1", len(testElement))

## //XPath Conditions
testElement = driver.find_elements(By.XPATH,"//input[@maxlength<=15 and @name='name' and @type='text']")
print(" elements size 2", len(testElement))

testElement = driver.find_elements(By.XPATH,"//input[@maxlength<=15 or @name='namgge' or @type='tegggxt']")
print(" elements size 3", len(testElement))


testElement = driver.find_elements(By.XPATH,"//input[@maxlength<=15 or @name='namgge' or @type='tegggxt']")
print(" elements size 4", len(testElement))
## x path Functions

driver.find_element(By.XPATH,"//a[text()='Sign in']").get_attribute("text")
print(driver.find_element(By.XPATH,"//a[contains(text(),'account')]").get_attribute("text"))
driver.find_element(By.XPATH,"//div[contains(@class,'signin')]")
driver.find_element(By.XPATH,"//a[starts-with(text(),'Sign in into')]")
driver.find_element(By.XPATH,"//label[normalize-space(text())='First Name']")
driver.find_element(By.XPATH,"(//table[@id='contactList']/tbody/tr)[last()]")


## XPath Aces  //https://www.w3schools.com/xml/xpath_axes.asp
"""
XPath Axes
An axis represents a relationship to the context (current) node, and is used to locate nodes relative to that node on the tree.


"""
driver.find_element(By.XPATH,"//label[text()='Email']/following-sibling::input[@type='text']")
driver.find_element(By.XPATH,"//td[text()='Maria Anders']/preceding-sibling::td/child::input")
driver.find_element(By.XPATH, "//label[text()='Password']/following::input")

## XPATH Shortcuts
"""
// text() -> .
Instead of text() we can use .
"""
driver.find_element(By.XPATH,"//h1[.='Register']")
driver.find_element(By.XPATH,"//a[contains(.,'account')]")
driver.find_element(By.XPATH,"//td[starts-with(.,'Maria')]")
driver.find_element(By.XPATH,"//label[normalize-space(.)='First Name']")

"""
child -> /
Instead of child() we can use .
"""
driver.find_element(By.XPATH,"//div[@class='container']/h1")

"""
//parent - > /..
Instead of child() we can use .
"""
driver.find_element("//h1[.='Register']/..")
		

driver.close()