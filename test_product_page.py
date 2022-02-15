import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
param = "/?promo=offer"
url = link + param
links = [url+str(i) for i in range(10)]
xfail = 7
links[xfail] = pytest.param(links[xfail], marks=pytest.mark.xfail(reason="some bug"))

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    """

    The test checks the possibility of adding an item to the shopping cart 
    
    on the promo page and the appearance of a message if successful

    """
    
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_item_to_cart()
    page.product_name_matches()
    page.should_be_message_about_cost_of_basket()
    page.compare_cost_of_basket_with_product_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """ 

    The test checks if there is no message about adding 
    
    an item to the cart after adding an item to the cart

    """

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_message_about_item_to_cart()

def test_guest_cant_see_success_message(browser):
    """ 
    
    The test checks if there is no message about adding 
    
    an item to the cart after opening the page

    """
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_message_about_item_to_cart()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """

    The test checks if there is no message about adding

    an item to the cart after adding an item to the cart.

    Using is_disappeared.

    """

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_be_disappeared_message_about_item_to_cart()

def test_guest_should_see_login_link_on_product_page(browser):
    """ The guest can see the login link on the product page """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    """ The guest can go to the login page from the page """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """ 
    
    The test checks that the shopping cart is empty 
    
    when navigating from the main page

    """
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_text_that_basket_is_empty()


