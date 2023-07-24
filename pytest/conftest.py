import pytest

@pytest.fixture(scope="class")
def setup():
    print('I will be executing first from fixture setup method as pre-requisite from conftest.py file.')
    yield               # Whatever is there after 'yield' keyword it will ex3cute after testcase execution.
    print('I will be executing last from fixture setup method as post-requisite from conftest.py file.')
