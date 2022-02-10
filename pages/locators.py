from selenium.webdriver.common.by import By


class MainPageLocators():
    """ Locators for the main page.

    The class contains information about how and which element to search for.

    """

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """Locators for the login page.

    The class contains information about how and which element to search for.

    """

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")




