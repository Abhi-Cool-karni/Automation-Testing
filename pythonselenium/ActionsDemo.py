from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)

# action.click_and_hold() #long press
# action.context_click()
# action.double_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(
    By.ID, "mousehover")).perform()  # hover the element
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(
    By.LINK_TEXT, "Reload")).click().perform()