import pytest
from PageObjectMechanism.HomePage import HomePage
from TestData.HomePageData import HomepageData
from Utility.BaseClass import baseClass


class TestHomePage(baseClass):

    def test_FormSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["Name"])  # NAME
        homepage.getEmail().send_keys(getData["Email"])  # EMAIL
        homepage.getPassword().send_keys(getData["Password"])  # PASSWORD
        homepage.getCheckbox().click()  # CHECKBOX
        self.selectOptioByText(homepage.selectDropdown(), getData["Gender"])  # GENDER SELECTION
        homepage.ClickRadio().click()  # Employment Status
        homepage.clickSubmit().click()  # Submit button
        message = homepage.getSuccess()
        print(message)
        assert "Success" in message
        self.driver.refresh()

    # Implementing Data driven mechanism by removing hard coding data from tests
    # @pytest.fixture(params=[("Abhishek", "abhishekkul000@gmail.com", "abhishek@1234", "Male"), ("Priya", "priya@gmail.com", "priya@1234", "Female")])
    # Params supports both tuple and dictionary
    @pytest.fixture(params=HomepageData.test_Homepage_Data)
    def getData(self, request):
        return request.param
