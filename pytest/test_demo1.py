
#* Any pytest file should start with test_ or end with _test.	
#* pytest method names should start with test.
#* Any code should be wrapped in method only.
#* In pytest every method is treated as testcase.
#* Method name should have sense.
#* -k stands for method names execution, -s logs in output, -v stands for more info metadata	
#* You can run specific file with py.test <filename>
#* You can mark (tag) tests @pytest.mark.<tagname> and then run with - m
#* You can skip tests with @pytest.mark.skip. 
#* You can make test run but not allowed to report with @pytest.mark.xfail
#* You can make testcase pre-requisites, post-requisites run by @pytest.fixture()  
#* Instead of duplicating task like browser invoking for each testcase instead we can use conftest.py which will common for all pytest files.
#* Fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixture and make it available to all test cases.
#* Datadriven and parameterization can be done with return statements in tuple format	
#* #when you define fixture scope to class only, it will run once before class initiated and at the end.	


import pytest


@pytest.mark.smoke
def test_firstGreet():
    print("Hello")	

@pytest.mark.xfail
def test_secondGreet(setup):
    print("Good Morning")	



# ! To run test case from command prompt
# TODO py.test               --> To run all test cases.
# * OUTPUT => 
# ? ====================================== test session starts =======================================
# ? platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.0.0
# ? rootdir: C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest
# ? plugins: anyio-3.7.0
# ? collected 1 item
# ? test_demo1.py .                                                                             [100%]
# ? ======================================= 1 passed in 0.11s ========================================

# TODO py.test -v (verbose)  --> To get more details of test case result execution.
# * OUTPUT => 
# ? ======================================================= test session starts ========================================================
# ? platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.0.0 -- C:\Users\Abhishek Kulkarni\AppData\Local\Programs\Python\Python311\python.exe
# ? cachedir: .pytest_cache
# ? rootdir: C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest
# ? plugins: anyio-3.7.0
# ? collected 1 item
# ? test_demo1.py::test_firstProgram PASSED                                                                                       [100%]
# ? ======================================================== 1 passed in 0.08s =========================================================

# TODO py.test -v -s         --> To see the console log result of test case execution.
# * OUTPUT =>
# ? ==================================================================== test session starts ====================================================================
# ? platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.0.0 -- C:\Users\Abhishek Kulkarni\AppData\Local\Programs\Python\Python311\python.exe
# ? cachedir: .pytest_cache
# ? rootdir: C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest
# ? plugins: anyio-3.7.0
# ? collected 1 item
# ? test_demo1.py::test_firstProgram Hello
# ? PASSED
# ? ===================================================================== 1 passed in 0.04s =====================================================================