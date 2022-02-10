from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """The main page. 
    
    The class associated with the main page.

    """

    def go_to_login_page(self):
        """ Go to the authorization page """
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """ Will check for the  login link """
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK),"Login is not present"


