from selenium.webdriver.common.by import By
from Utility.BaseClass import baseClass
from PageObjectMechanism.HomePage import HomePage


class TestOne(baseClass):
    def test_e2e(self):
        # logging
        log = self.getLogger()
        # Homepage
        log.info("Invoking browser and redirecting to link and filling form.")
        homePage = HomePage(self.driver)

        # Integrating point between homepage and shop page
        checkoutPage = homePage.shopItems()
        log.info("clicking on shop text link")
        # Checkoutpage
        # Getting list of cards
        cards = checkoutPage.getCardTitles()
        log.info('getting card details')
        # selecting and checking out the Blackberry product
        for card in cards:
            cardName = card.find_element(By.XPATH, "div/h4/a").text
            log.info(cardName)
            if cardName == "Blackberry":
                card.find_element(By.XPATH, "div/button").click()

        # Moving to checkout page
        checkoutPage.CheckoutBtn().click()

        # Making checkout of product
        # Integrating point between shop page and checkoutpage
        confirmpage = checkoutPage.productcheckout()

        # Confirmpage

        # Selecting location for checkout
        confirmpage.selectlocation().send_keys("Ind")
        log.info("Entering country name as Ind")

        # Waiting till location is load and displayed
        self.verifyLinktextPresence("India")
        confirmpage.getLocation().click()

        # Clicking an checkbox
        confirmpage.clickingCheckbox().click()

        # Submitting location
        confirmpage.doLocationSubmit().click()

        # Success validation
        successMessage = confirmpage.successMessage().text
        log.info("Text received form application "+successMessage)
        assert "Success!" in successMessage
