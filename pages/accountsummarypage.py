from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class AccountSummaryPage(BasePage):

    PAYBILLS_LINK = (By.XPATH,"//a[text()='Pay Bills']")

    def click_paybillslink(self):
        self.click(self.PAYBILLS_LINK)