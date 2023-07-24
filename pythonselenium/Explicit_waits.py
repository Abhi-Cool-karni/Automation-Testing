# Implicit waits and Explicits waits

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
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

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)  # 48+160+180 = 388

print("Total Amount =", sum)

totalAmnt = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == totalAmnt

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(
    "rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# Explicit wait - In explicit wait we can target one specific element and we can set explicit/exclusively to that particular upto 15 sec.
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(
    (By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# totAmt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
discAmt = float(driver.find_element(
    By.XPATH, "//span[@class='discountAmt']").text)

assert discAmt < totalAmnt
print("Discount amount =", discAmt)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
