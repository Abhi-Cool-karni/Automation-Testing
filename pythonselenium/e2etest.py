from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service(
    "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Regular expression - instead of targeting value full give piece of information.
# CSS - a[href*='shop']  Xpath - //a[contains(@href,'shop')]

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# selecting and checking out the Blackberry product
for card in cards:
    cardName = card.find_element(By.XPATH, "div/h4/a").text
    if cardName == "Blackberry":
        card.find_element(By.XPATH, "div/button").click()

# Moving to checkout page
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# Making checkout of product
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

# Selecting location for checkout
driver.find_element(By.ID, "country").send_keys("Ind")

# Waiting till location is load and displayed
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((
    By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

# Clicking an checkbox
driver.find_element(
    By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

# Submitting location
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

# Success validation
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success!" in successText

driver.close()
