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
driver.get("https://leveredgetesting.hulcd.com/rsunify/")
time.sleep(2)
driver.find_element(By.ID, "userName").send_keys("SA")

try:
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Unilever@12345")

except Exception as e:
    print(e)

driver.find_element(By.ID, "databaseName").send_keys("135018")