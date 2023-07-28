from selenium.webdriver.common.by import By

from PageObjectMechanism.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # cardText = (By.XPATH, "div/h4/a")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)
    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")


    # Moving to checkout page
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    clickCheckoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def CheckoutBtn(self):
        return self.driver.find_element(*CheckoutPage.clickCheckoutButton)

    # Making checkout of product
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    productCheckout = (By.XPATH, "//button[@class='btn btn-success']")

    def productcheckout(self):
        self.driver.find_element(*CheckoutPage.productCheckout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
