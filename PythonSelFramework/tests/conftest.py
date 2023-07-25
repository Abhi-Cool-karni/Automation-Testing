from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture(scope="class")
def setup(request):

    service_obj = Service("C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()