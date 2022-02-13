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


class ProductPageLocators():
    """Locators for the product page.

    The class contains information about how and which element to search for.

    """

    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-primary.btn-add-to-basket")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".breadcrumb .active")
    MESSAGE_CART_COST = (By.CSS_SELECTOR, "#messages>:nth-child(3) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


