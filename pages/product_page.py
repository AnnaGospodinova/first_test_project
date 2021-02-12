from .base_page import BasePage
from .locators import PageObjectLocators


class PageObject(BasePage):

	def add_to_basket(self):
		add_button = self.browser.find_element(*PageObjectLocators.BUTTON_ADD_TO_BASKET)
		add_button.click()

	def should_be_message_about_adding(self):
		product_name = self.browser.find_element(*PageObjectLocators.PRODUCT_NAME).text
		message_about_adding = self.browser.find_element(*PageObjectLocators.MESSAGE_ABOUT_ADDING).text
		assert product_name == message_about_adding, "No product name in message"

	def should_be_true_total_price(self):
		product_price = self.browser.find_element(*PageObjectLocators.PRODUCT_PRICE).text
		total_price = self.browser.find_element(*PageObjectLocators.TOTAL_PRICE_IN_MESSAGE_ABOUT_TOTAL_PRICE).text
		assert product_price == total_price, "Total price is not like product price"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def should_will_be_success_message(self):
		assert self.is_disappeared(*PageObjectLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
	
	