# Implicit waits and Explicits waits

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)
# Implicit wait
driver.implicitly_wait(5)
# Global timeout for script
# Script waits waits for MAX 5 seconds, If element found in 2 then script will continue.
# 5 seconds is MAX Timeout.. 2 seconds (3 seconds save)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
productsLen = len(products)
assert productsLen > 0
print("count of products = ", productsLen)
#  Chaining of web elements
for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(
    "rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

