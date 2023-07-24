from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# CSSselector - tagname[attributename='attribute value'] ex: input[type='submit']
driver.find_element(
    By.CSS_SELECTOR, "input[name='name']").send_keys('Rahul')

# other tricks for CSS selectors
# by #idvalue
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# ID, CLASS NAME, NAME, etc
driver.find_element(By.NAME, "email").send_keys("rahul@example.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("rahul@1234")
driver.find_element(By.ID, "exampleCheck1").click()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
# dropdown.select_by_value() # As we don't have value in current page

# Xpath - //tagname[@attributename='attribute value'] ex: //input[@type='submit']
# click submit button
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

# assert if failed then assert message will show

# Another trick for Xpath for select one in multiple ex: selecting last edit box in list of 3 edit box
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(
    By.XPATH, "(//input[@type='text'])[3]").send_keys(" Abhishek")
