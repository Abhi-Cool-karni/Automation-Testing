from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import pytest

# Command line option or Hook
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/chromedriver_win32/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        service_obj = Service("C:/Users/Abhishek Kulkarni/Desktop/AK/Software Testing/Automation/msedgedriver")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
