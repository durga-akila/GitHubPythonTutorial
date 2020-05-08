from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class PayBillsPage(BasePage):

    ADDNEWPAYEELINK = (By.XPATH,"//a[text()='Add New Payee']")
    NAME_FIELD = (By.ID,'np_new_payee_name')
    ADDRS_FIELD = (By.ID,'np_new_payee_address')
    ACC_FIELD = (By.ID,'np_new_payee_account')
    DETAILS_FIELD = (By.ID, 'np_new_payee_details')
    ADD_BUTTON = (By.ID,'add_new_payee')

    def click_addnewpayeelink(self):
        self.click(self.ADDNEWPAYEELINK)

    def add_payee(self,name,addrs,acc,details):
        self.wait_for_element(self.NAME_FIELD,"visibility").send_keys(name)
        self.type(self.ADDRS_FIELD, addrs)
        self.type(self.ACC_FIELD, acc)
        self.type(self.DETAILS_FIELD, details)
        self.click(self.ADD_BUTTON)


