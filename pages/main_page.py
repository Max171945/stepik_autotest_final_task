from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """The main page. 
    
    The class associated with the main page.

    """

    def go_to_login_page(self):
        """ Go to the authorization page """
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """ Will check for the link """
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"),"Login is not present"


