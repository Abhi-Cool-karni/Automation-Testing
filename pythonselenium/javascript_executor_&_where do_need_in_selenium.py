# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


# Headless mode - running chrome in background executing test cases without chrome UI interaction.

chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Scrolling automate
driver.execute_script("window.scroll(0,400);")
driver.get_screenshot_as_file("screen.png")
driver.execute_script("window.scroll(0,document.body.scrollHeight);")

# Taking screenshots using python to trigger JS to take screenshot.
driver.get_screenshot_as_file("screen_bottom.png")
