from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """The main page. 
    
    The class associated with the main page.

    """

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


