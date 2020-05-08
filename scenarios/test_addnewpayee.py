import pytest
from ctreport_selenium.ctlistener import Test
from ctreport_selenium.utility_classes import Priority

from pages.accountsummarypage import AccountSummaryPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.paybillspage import PayBillsPage
from testdata.readdata import getdata


@pytest.fixture(scope="module",autouse=True)
def navigate_to_paybills(driver):
    home = HomePage(driver)
    home.click_signin_button()
    login = LoginPage(driver)
    login.do_login("username","password")
    acc = AccountSummaryPage(driver)
    acc.click_paybillslink()

@pytest.fixture
def navigate_to_addnewpayee(driver):
    paybills = PayBillsPage(driver)
    paybills.click_addnewpayeelink()

    yield
    test.finish()

@pytest.mark.parametrize("name,addrs,acc,detail",getdata())
def test_01(driver, navigate_to_addnewpayee,name,addrs,acc,detail):
    global test
    test = Test("Add New payee: payee name: " +  name,
                description="Add new payee sceario validation",
                priority=Priority.HIGH)
    test.log("Navigated successfully to Add New Payee page")
    paybills = PayBillsPage(driver)
    paybills.add_payee(name,addrs,acc,detail)
    test.take_screenshot()
    test.verify_are_equal("Hello","Hello","sdjkagsdfjgjlahfgj",onfail_screenshot=True)
