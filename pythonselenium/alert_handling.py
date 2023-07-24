import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Abhishek"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
# switch to alert mode
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
# To click ok button
assert name in alertText
time.sleep(2)
alert.accept()

# To click cancel button
# alert.dismiss()
