import pytest


# Grouping or tagging the smoke testcase 
@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondProgram():
    a,b=4,6
    assert a+2 == 6, "Addition do not match"

def test_fixtureDemo1(setup):
    print(' I will be executing in fixtureDemo1 method after setup execution from test_demo2.py file.')


# ! TO run specific files.
# TODO py.test test_demo2.py -v -s      --> This will run only selected file.
# * OUTPUT =>
# ? ==================================================================== test session starts ====================================================================
# ? platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.0.0 -- C:\Users\Abhishek Kulkarni\AppData\Local\Programs\Python\Python311\python.exe
# ? cachedir: .pytest_cache
# ? rootdir: C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest
# ? plugins: anyio-3.7.0
# ? collected 2 items
# ? test_demo2.py::test_message FAILED
# ? test_demo2.py::test_addition PASSED
# ? ========================================================================= FAILURES ==========================================================================
# ? _______________________________________________________________________ test_message ________________________________________________________________________
# ?     def test_message():
# ?         msg = "Hello"
# ? >       assert msg == "Hi", "Test failed because strings do not match"
# ? E       AssertionError: Test failed because strings do not match
# ? E       assert 'Hello' == 'Hi'
# ? E         - Hi
# ? E         + Hello
# ? test_demo2.py:5: AssertionError
# ? ================================================================== short test summary info ==================================================================
# ? FAILED test_demo2.py::test_message - AssertionError: Test failed because strings do not match
# ? ================================================================ 1 failed, 1 passed in 1.07s ================================================================


# ! To run specific testcase name from multiple files
# TODO py.test -k Program -v -s          --> This will run only testcase which contains 'Program' text in testcase name/method from multiple files.
# * OUTPUT =>
# ? ==================================================================== test session starts ====================================================================
# ? platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.0.0 -- C:\Users\Abhishek Kulkarni\AppData\Local\Programs\Python\Python311\python.exe
# ? cachedir: .pytest_cache
# ? rootdir: C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest
# ? plugins: anyio-3.7.0
# ? collected 4 items / 2 deselected / 2 selected
# ? test_demo2.py::test_firstProgram FAILED
# ? test_demo2.py::test_secondProgram PASSED
# ? ========================================================================= FAILURES ==========================================================================
# ? _____________________________________________________________________ test_firstProgram _____________________________________________________________________
# ?     def test_firstProgram():
# ?         msg = "Hello"
# ? >       assert msg == "Hi", "Test failed because strings do not match"
# ? E       AssertionError: Test failed because strings do not match
# ? E       assert 'Hello' == 'Hi'
# ? E         - Hi
# ? E         + Hello
# ? test_demo2.py:5: AssertionError
# ? ================================================================== short test summary info ==================================================================
# ? FAILED test_demo2.py::test_firstProgram - AssertionError: Test failed because strings do not match
# ? ========================================================= 1 failed, 1 passed, 2 deselected in 0.41s =========================================================

# ! Grouping or tagging the smoke testcase 
# TODO py.test -m smoke -v -s       --> This will run only marked (-m) testcase
# * OUTPUT =>
# ? ====================================== test session starts =======================================
# ? platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.0.0 -- C:\Users\Abhishek Kulkarni\AppData\Local\Programs\Python\Python311\python.exe
# ? cachedir: .pytest_cache
# ? rootdir: C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest
# ? plugins: anyio-3.7.0
# ? collected 4 items / 2 deselected / 2 selected
# ? test_demo1.py::test_firstGreet Hello
# ? PASSED
# ? test_demo2.py::test_firstProgram FAILED
# ? ============================================ FAILURES ============================================
# ? _______________________________________ test_firstProgram ________________________________________
# ?     @pytest.mark.smoke
# ?     def test_firstProgram():
# ?         msg = "Hello"
# ? >       assert msg == "Hi", "Test failed because strings do not match"
# ? E       AssertionError: Test failed because strings do not match
# ? E       assert 'Hello' == 'Hi'
# ? E         - Hi
# ? E         + Hello
# ? test_demo2.py:7: AssertionError
# ? ======================================== warnings summary ========================================
# ? test_demo1.py:13
# ?   c:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest\test_demo1.py:13: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
# ?     @pytest.mark.smoke
# ? test_demo2.py:4
# ?   c:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest\test_demo2.py:4: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
# ?     @pytest.mark.smoke
# ? -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ? ==================================== short test summary info =====================================
# ? FAILED test_demo2.py::test_firstProgram - AssertionError: Test failed because strings do not match
# ? ===================== 1 failed, 1 passed, 2 deselected, 2 warnings in 1.20s ======================

# ! Skipping testcase
# TODO  py.test -v -s       --> Run all test cases now 1 testcase is skipped due to @pytest.mark.skip.
# * OUTPUT=>
# ? ===================================================================== test session starts =====================================================================
# ? platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.0.0 -- C:\Users\Abhishek Kulkarni\AppData\Local\Programs\Python\Python311\python.exe
# ? cachedir: .pytest_cache
# ? rootdir: C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest
# ? plugins: anyio-3.7.0
# ? collected 4 items
# ? test_demo1.py::test_firstGreet Hello
# ? PASSED
# ? test_demo1.py::test_secondGreet Good Morning
# ? PASSED
# ? test_demo2.py::test_firstProgram SKIPPED (unconditional skip)
# ? test_demo2.py::test_secondProgram PASSED
# ? ====================================================================== warnings summary =======================================================================
# ? test_demo1.py:14
# ?   c:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest\test_demo1.py:14: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
# ?     @pytest.mark.smoke
# ? test_demo2.py:4
# ?   C:\Users\Abhishek Kulkarni\Desktop\AK\Software Testing\Automation\pytest\test_demo2.py:4: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
# ?     @pytest.mark.smoke
# ? -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ? ========================================================== 3 passed, 1 skipped, 2 warnings in 0.25s ===========================================================