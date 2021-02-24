from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTRATION_EMAIL = (By.NAME, "registration-email")
	PASSWORD = (By.NAME, "registration-password1")
	CONFIRM_PASSWORD = (By.NAME, "registration-password2")
	REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class PageObjectLocators():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner strong")
	TOTAL_PRICE_IN_MESSAGE_ABOUT_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_OBJECT = (By.CSS_SELECTOR, "#basket_formset")
	BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
