from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
openedWindows = driver.window_handles

# controls transferred to child window.
driver.switch_to.window(openedWindows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

# Controls transferred to parent from child win
driver.switch_to.window(openedWindows[0])

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

print(driver.find_element(By.TAG_NAME, "h3").text)
