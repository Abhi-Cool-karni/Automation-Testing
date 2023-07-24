# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

BrowserSortedveggieList = []

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all viggiew names -> BrowserSortedveggieList (A,B,C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for element in veggieWebElements:
    BrowserSortedveggieList.append(element.text)

originalBrowserSortedveggieList = BrowserSortedveggieList.copy()
print("originalBrowserSortedveggieList: \n",originalBrowserSortedveggieList)

# Sort this BrowserSortedveggieList => newSortedList (A,B,C)
BrowserSortedveggieList.sort()
print("BrowserSortedveggieList: \n",BrowserSortedveggieList)

# BrowserSortedveggieList == newSortedList
assert BrowserSortedveggieList == originalBrowserSortedveggieList
