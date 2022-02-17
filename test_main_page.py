import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    """ The test for main page.

    The class tests the transition from the main page to the login page.

    """
    
    link = "http://selenium1py.pythonanywhere.com/"

    def test_guest_can_go_to_login_page(self, browser):
        """ Test of going to the login page """
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
    def test_guest_should_see_login_link(self, browser):
        """ The test checks for a link to the login page """
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """ 
    
    The test checks that the shopping cart is empty when 
    
    navigating from the main page

    """

    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_text_that_basket_is_empty()


