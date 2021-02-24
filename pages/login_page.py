from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert "/login/" in self.url, "Word login not in url"
		assert True

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"		
		assert True

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"
		assert True

	def  register_new_user(self, email, password):
		input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
		input_email.send_keys(email)
		input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
		input_password.send_keys(password)
		input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
		input_confirm_password.send_keys(password)
		registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
		registration_button.click()

		