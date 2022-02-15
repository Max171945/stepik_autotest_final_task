from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """ The basket page.

    The class associated with the basket page.

    """

    def should_be_product_in_basket(self):
        """ The method checks that there is an item in the cart """
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET),\
                "The basket is empty"

    def should_not_be_product_in_basket(self):
        """ The method checks that there is no product in the cart """
        assert self.is_not_element_present(
                *BasketPageLocators.PRODUCT_IN_BASKET), "The basket isn't empty"
    
    def should_be_text_that_basket_is_empty(self):
        """ 
        
        The method checks for the presence of the text 

        that the basket is empty
        
        """
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY),\
                "There is no message that the basket is empty"

    def should_not_be_text_that_basket_is_empty(self):
        """ 
        
        The method checks for the absence of the text 

        that the basket is empty
        
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY),\
                "There is a message that the basket is empty"


