from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Utility.BaseClass import baseClass

class TestOne(baseClass):
    def test_e2e(self):
        # Regular expression - instead of targeting value full give piece of information.
        # CSS - a[href*='shop']  Xpath - //a[contains(@href,'shop')]

        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        cards = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        # selecting and checking out the Blackberry product
        for card in cards:
            cardName = card.find_element(By.XPATH, "div/h4/a").text
            if cardName == "Blackberry":
                card.find_element(By.XPATH, "div/button").click()

        # Moving to checkout page
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        # Making checkout of product
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        # Selecting location for checkout
        self.driver.find_element(By.ID, "country").send_keys("Ind")

        # Waiting till location is load and displayed
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((
            By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        # Clicking an checkbox
        self.driver.find_element(
            By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        # Submitting location
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        # Success validation
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success!" in successText
