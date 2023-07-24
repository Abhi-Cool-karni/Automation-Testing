from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
#  LINK TEXT
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "password?").click()

# Locate by TAGNAME  parent to child - xpath ex: //form/div[1]/input in form first div is selected out of 3 under that selected input element

driver.find_element(
    By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")  # email
driver.find_element(
    By.XPATH, "//form/div[2]/input").send_keys("demo@")  # password

#  similarly for CSS instead of / use space and // is not required
# confirm password
driver.find_element(
    By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("demo@")

# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# SELECT TEXT based locators ex: //button[text()='Save New Password']
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

driver.close()
