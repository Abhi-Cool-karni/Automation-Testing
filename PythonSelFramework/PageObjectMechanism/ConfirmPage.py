from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # Selecting location for checkout
    selectLocation = (By.ID, "country")

    def selectlocation(self):
        return self.driver.find_element(*ConfirmPage.selectLocation)

    # Load location
    # self.driver.find_element(By.LINK_TEXT, "India").click()
    location = (By.LINK_TEXT, "India")

    def getLocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    # Clicking a checkbox
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    clickCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def clickingCheckbox(self):
        return self.driver.find_element(*ConfirmPage.clickCheckbox)

    # Submitting location
    # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    locationSubmit = (By.CSS_SELECTOR, "[type='submit']")

    def doLocationSubmit(self):
        return self.driver.find_element(*ConfirmPage.locationSubmit)

    # Success validation
    # self.driver.find_element(By.CLASS_NAME, "alert-success").text
    successtext = (By.CLASS_NAME, "alert-success")

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.successtext)
