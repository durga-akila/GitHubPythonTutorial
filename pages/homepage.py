from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class HomePage(BasePage):

    SIGNIN_BUTTON = (By.ID,"signin_button")

    def click_signin_button(self):
        self.click(self.SIGNIN_BUTTON)