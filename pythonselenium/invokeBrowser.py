#  Chrome driver is a intermediate file from selenium test and is responsible to invoke
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
try:
    service_obj = Service(
        "C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
    driver = webdriver.Chrome(service=service_obj)

    driver.maximize_window()  # To maximize the window of browser
    driver.get("https://rahulshettyacademy.com")  # Hit URL on the browser
    # to get title of the web page ex: Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy
    print(driver.title)
    # to get the current url of the page ex: https://rahulshettyacademy.com/
    print(driver.current_url)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    print(driver.current_url)
    driver.back()  # go back to previous page
    driver.forward()  # move forward to recent page
    driver.refresh()  # refresh the page
    # driver.minimize_window()

except Exception as e:
    # Handle the exception
    print("An exception occurred:", str(e))
