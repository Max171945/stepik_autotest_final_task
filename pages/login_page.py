from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """ The login page.

    The class associated with the login page.

    """

    def should_be_login_page(self):
        """ The method checks the login page """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """ Checking for the correct url """
        login_url = self.browser.current_url
        assert 'login' in login_url, f"Incorrect URL: {login_url}"

    def should_be_login_form(self):
        """ Checking that there is a login form """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
                "There is no login form on the page"

    def should_be_register_form(self):
        """ Checking that there is a registration form on the page """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
                "There is no registration form on the page"

    def register_new_user(self, email, password):
        """ The method adds a new user """
        register_email = self.browser.find_element(
                *LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        register_password = self.browser.find_element(
                *LoginPageLocators.REGISTER_PASSWORD)
        register_password.send_keys(password)
        register_password2 = self.browser.find_element(
                *LoginPageLocators.REGISTER_PASSWORD2)
        register_password2.send_keys(password)
        register_button = self.browser.find_element(
                *LoginPageLocators.REGISTER_BUTTON)
        register_button.click()



