from .pages.product_page import PageObject
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6", pytest.param ("7", marks=pytest.mark.xfail(reason="bug")), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, number):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
	page = PageObject(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_message_about_adding()
	page.should_be_true_total_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject (browser, link)
	page.open()
	page.add_to_basket()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject (browser, link)
	page.open()
	page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject (browser, link)
	page.open()
	page.add_to_basket()
	page.should_will_be_success_message()

@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject(browser, link)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject(browser, link)
	page.open()
	page.go_to_basket()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_not_element_in_basket()
	basket_page.should_be_text_about_empty_basket()

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time()) + "1q2w3e"
		page = LoginPage(browser, link)
		page.open()
		page.go_to_login_page()
		page.register_new_user(email, password)
		page.should_be_authorized_user()	
	
	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = PageObject(browser, link)
		page.open()
		page.add_to_basket()
		page.should_be_message_about_adding()
		page.should_be_true_total_price()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = PageObject(browser, link)
		page.open()
		page.should_not_be_success_message()


	