import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("In")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries), "countries")

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text)
assert driver.find_element(
    By.ID, "autosuggest").get_attribute("value") == "India"
