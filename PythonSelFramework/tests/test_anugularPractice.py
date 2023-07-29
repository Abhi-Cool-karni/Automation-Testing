from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjectMechanism.HomePage import HomePage
from Utility.BaseClass import baseClass


class TestHomePage(baseClass):

    def test_FormSubmission(self):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys('Abhishek') #NAME
        homepage.getEmail().send_keys("abhishekkul2000@gmail.com")  #EMAIL
        homepage.getPassword().send_keys("abhishek@1234")   #PASSWORD
        homepage.getCheckbox().click()  #CHECKBOX
        self.selectOptioByText(homepage.selectDropdown(), "Female") #GENDER SELECTION
        homepage.ClickRadio().click()   #Employment Status
        homepage.clickSubmit().click()  #Submit button
        message = homepage.getSuccess()
        print(message)
        assert "Success" in message
