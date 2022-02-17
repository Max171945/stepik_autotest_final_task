import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    """ The base page.
    
    The class of the base page from which all other classes will be inherited.

    """

    def __init__(self, browser, url):
        """ Creating a page object """
        self.browser = browser
        self.url = url
    
    def go_to_login_page(self):
        """ Go to the authorization page """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        """ Go to the basket page """
        basket = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket.click()

    def should_be_authorized_user(self):
        """ The method checks that the user is logged in """
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
                "User icon is not presented, probably unauthorised user"
    
    def should_be_login_link(self):
        """ Will check for the  login link """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
                "Login is not present"
    
    def open(self):
        """ The method opens the desired page in the browser """
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=4):
        """ The method checks for the presence of an element on the page """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """ The method checks the absence of an element for a specified time """
        return not self.is_element_present(how, what, timeout)
        
    def solve_quiz_and_get_code(self):
        """ 
       
        The method considers the result of a mathematical expression
        
        and enters the answer

        """

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_disappeared(self, how, what, timeout=4):
        """
        
        The method checks the disappearance of an element for a certain time

        """

        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                    until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


