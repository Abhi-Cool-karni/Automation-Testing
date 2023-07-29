from selenium.webdriver.common.by import By
from Utility.BaseClass import baseClass
from PageObjectMechanism.HomePage import HomePage


class TestOne(baseClass):
    def test_e2e(self):
        # Homepage
        homePage = HomePage(self.driver)

        # Integrating point between homepage and shop page
        checkoutPage = homePage.shopItems()

        # Checkoutpage
        # Getting list of cards
        cards = checkoutPage.getCardTitles()

        # selecting and checking out the Blackberry product
        for card in cards:
            cardName = card.find_element(By.XPATH, "div/h4/a").text
            if cardName == "Blackberry":
                card.find_element(By.XPATH, "div/button").click()

        # Moving to checkout page
        checkoutPage.CheckoutBtn().click()

        # Making checkout of product
        # Integrating point between shop page and checkoutpage
        confirmpage = checkoutPage.productcheckout()

        # Confirmpage
        # Selecting location for checkout
        # Sending Ind keys into location edit box
        confirmpage.selectlocation().send_keys("Ind")

        # Waiting till location is load and displayed
        self.verifyLinktextPresence("India")
        confirmpage.getLocation().click()

        # Clicking an checkbox
        confirmpage.clickingCheckbox().click()

        # Submitting location
        confirmpage.doLocationSubmit().click()

        # Success validation
        successMessage = confirmpage.successMessage().text

        assert "Success!" in successMessage
