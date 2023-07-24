import pytest
# scope='class' as an argument in fixture so that fixture can run once onn class level before the executing class.
# It will apply fixtures automatically to the methods in class.

@pytest.mark.usefixtures("setup")
class TestExample:
    
    def test_fixtureDemo(self):
        print(' I will be executing in fixtureDemo method after setup execution.')

    def test_fixtureDemo1(self):
        print(' I will be executing in fixtureDemo1 method after setup execution.')

    def test_fixtureDemo2(self):
        print(' I will be executing in fixtureDemo2 method after setup execution.')

    def test_fixtureDemo3(self):
        print(' I will be executing in fixtureDemo3 method after setup execution.')

    def test_fixtureDemo4(self):
        print(' I will be executing in fixtureDemo4 method after setup execution.')

    def test_fixtureDemo5(self):
        print(' I will be executing in fixtureDemo5 method after setup execution.')

    def test_fixtureDemo6(self):
        print(' I will be executing in fixtureDemo6 method after setup execution.')

    def test_fixtureDemo7(self):
        print(' I will be executing in fixtureDemo7 method after setup execution.')

    def test_fixtureDemo8(self):
        print(' I will be executing in fixtureDemo8 method after setup execution.')

    def test_fixtureDemo9(self):
        print(' I will be executing in fixtureDemo9 method after setup execution.')

    def test_fixtureDemo10(self):
        print('I will be executing in fixtureDemo10 method after setup execution.')
