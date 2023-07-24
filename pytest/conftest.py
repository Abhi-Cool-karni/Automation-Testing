import pytest

@pytest.fixture(scope="class")
def setup():
    print('I will be executing first from fixture setup method as pre-requisite from conftest.py file.')
    yield               # Whatever is there after 'yield' keyword it will ex3cute after testcase execution.
    print('I will be executing last from fixture setup method as post-requisite from conftest.py file.')

# We can send data through fixtures to test. 
@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Abhishek","Kulkarni","abhishekkul2000@gmail.com"]


# Driving multiple sets of data through fixtures.

@pytest.fixture(params=[('chrome','Abhishek', 'Kulkarni'),('firefox','IE')])
def crossBrowser(request):
    return request.param