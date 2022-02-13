from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """ The product page.

    The class associated with the product page.

    """

    def add_product_to_card(self):
        """ The method adds an item to the cart """
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        


    def should_be_add_to_basket_button(self):
        """ 
        The method checks for the presence of
        
        a button to add an item to the cart 
        
        """

        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "The add to cart button is missing on the page"

    def should_be_message_about_adding_item_to_cart(self):
        """ 
        
        The method checks for a message about 
        
        adding an item to the cart

        """

        assert self.is_element_present(*ProductPageLocators.ADD_MESSAGE), "There is no message about adding an item to the cart"

    def product_name_matches(self):
        """ 
        Compares the name of the product on the page
        
        and the added product in the cart

        """

        added_product = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text
        product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        
        assert added_product == product, "The name of the product on the page and the added product in the cart do not match"

    def should_be_message_about_cost_of_basket(self):
        """ 

        The method checks whether there is a message 
        
        about the cost of the product in the cart

        """

        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART_COST), "There is no message about the cost of the product in the cart"

    def compare_cost_of_basket_with_product_price(self):
        """
        
        Compares the price of the goods 
        
        and the cost of the goods in the basket

        NOTE: THE BASKET SHOULD BE EMPTY!!!

        """

        cost_of_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_COST).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert cost_of_basket == price, "The price of the goods and the cost of the goods in the basket do not match"


