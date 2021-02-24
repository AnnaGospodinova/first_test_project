from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
	def test_guest_can_go_to_login_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = MainPage(browser, link)
		page.open()
		page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = MainPage(browser, link)
		page.open()
		page.should_be_login_link()

def test_guest_should_see_login_form(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_login_form()

def test_guest_should_see_register_form(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_register_form()

def test_word_login_should_be_in_url(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_login_url()

@pytest.mark.smoke
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.go_to_basket()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_not_element_in_basket()
	basket_page.should_be_text_about_empty_basket()