from .pages.product_page import PageObject
import pytest

@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6", pytest.param ("7", marks=pytest.mark.xfail(reason="bug")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
	page = PageObject(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_message_about_adding()
	page.should_be_true_total_price()

@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject (browser, link)
	page.open()
	page.add_to_basket()
	page.should_not_be_success_message()

@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject (browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject (browser, link)
	page.open()
	page.add_to_basket()
	page.should_will_be_success_message()
	