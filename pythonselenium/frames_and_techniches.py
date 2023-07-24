# What are frames?
# Frames are nothing but embedded HTML which sits top over base HTML, Though it looks like part of page but they are different.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://the-internet.herokuapp.com/iframe")

# Enter in frame window
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys(
    "I am able to automate frames.")

# Switch back to default page.
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
