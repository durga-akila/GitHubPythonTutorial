from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID,'user_login')
    PASSWORD_FIELD = (By.ID,'user_password')
    SIGNIN_BUTTON = (By.NAME,'submit')

    def do_login(self, uname,pword):
        self.type(self.USERNAME_FIELD,uname)
        self.type(self.PASSWORD_FIELD, pword)
        self.click(self.SIGNIN_BUTTON)