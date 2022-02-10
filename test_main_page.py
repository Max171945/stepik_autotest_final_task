from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    """ Test of going to the login page """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


