from selenium.webdriver.common.by import By


class BasePageLocators():
    """ Locators.

    The class contains information about how and which element to search for.

    """

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini>.btn-group>a")


class MainPageLocators():
    """ Locators for the main page.

    The class contains information about how 
    
    and which element to search for on the main page.

    """

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """Locators for the login page.

    The class contains information about how 
    
    and which element to search for on the login page.

    """

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    """Locators for the product page.

    The class contains information about how
    
    and which element to search for on the product page.

    """

    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-primary.btn-add-to-basket")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".breadcrumb .active")
    MESSAGE_CART_COST = (By.CSS_SELECTOR, "#messages>:nth-child(3) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators():
    """Locators for the basket page.

    The class contains information about how

    and which element to search for on the product page.

    """

    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
