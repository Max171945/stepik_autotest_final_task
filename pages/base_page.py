from selenium.common.exceptions import NoSuchElementException


class BasePage():
    """ The base page.
    
    The class of the base page from which all other classes will be inherited.

    """

    def __init__(self, browser, url, timeout=10):
        """ Creating a page object """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ The method opens the desired page in the browser """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """ The method checks for the presence of an element on the page """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


