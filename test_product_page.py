import pytest
from .pages.product_page import ProductPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
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
    page.add_product_to_card()
    page.should_be_message_about_adding_item_to_cart()
    page.product_name_matches()
    page.should_be_message_about_cost_of_basket()
    page.compare_cost_of_basket_with_product_price()

    


    
