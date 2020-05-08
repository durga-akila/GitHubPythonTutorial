
from selenium.webdriver.support import expected_conditions as EC
#selenium interactions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver= driver

    def click(self,locator):
        element = self.driver.find_element(*locator)
        self.highlight(element)
        element.click()

    def type(self,locator, text):
        element = self.driver.find_element(*locator)
        self.highlight(element)
        element.send_keys(text)

    def wait_for_element(self, locator, cond):
        wait = WebDriverWait(self.driver, 5)
        if cond == "visibility":
            element = wait.until(EC.visibility_of_element_located(locator))
            self.highlight(element)
            return element
        elif cond == "clickable":
            return wait.until(EC.element_to_be_clickable(locator))

    def highlight(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, "border: 2px solid red")

