
class BasePage():
    """ The base page.
    
    The class of the base page from which all other classes will be inherited.

    """

    def __init__(self, browser, url):
        """ Creating a page object """
        self.browser = browser
        self.url = url

    def open(self):
        """ The method opens the desired page in the browser """
        self.browser.get(self.url)

