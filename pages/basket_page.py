from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_not_element_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_OBJECT), "Product is present in basket, but should not be"

	def should_be_text_about_empty_basket(self):
		basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
		assert "Your basket is empty" in basket_text, "Basket is not empty"