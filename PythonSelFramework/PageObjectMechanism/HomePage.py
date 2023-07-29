from selenium.webdriver.common.by import By

from PageObjectMechanism.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

# Homepage data
    name = (By.CSS_SELECTOR, "input[name='name']")
    inlineRadio = (By.CSS_SELECTOR, "#inlineRadio1")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropDown = (By.ID, "exampleFormControlSelect1")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectDropdown(self):
        return self.driver.find_element(*HomePage.dropDown)

    def ClickRadio(self):
        return self.driver.find_element(*HomePage.radio)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.message).text
