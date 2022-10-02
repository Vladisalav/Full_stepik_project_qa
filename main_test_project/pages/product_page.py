from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class MainPage(BasePage):
    pass

    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)
    #
    def should_be_login_page(self):
        self.should_be_open_basket_from_product()
        self.should_be_clean()
        # self.should_be_open_basket()
        # self.should_be_find_true_login_link()
        # self.test_should_be_add_to_basket()
        # self.solve_quiz_and_get_code()
        # self.should_be_name_product()
        # self.should_be_equally()
        # self.should_not_be_success_message()

    def should_be_open_basket_from_product(self):
        add_basket_product = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_basket_product.click()

    def should_be_clean(self):
        basket_product_message = self.browser.find_element(*ProductPageLocators.MESSAGE_CLEAN).text
        assert "Your basket is empty." in basket_product_message, "Not Clean"

    # def should_be_open_basket(self):
    #     add_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
    #     add_basket.click()
    #
    # def should_be_clean(self):
    #     basket_message = self.browser.find_element(*ProductPageLocators.MESSAGE_CLEAN).text
    #     assert "Your basket is empty." in basket_message, "Not Clean"

    # def should_be_find_true_login_link(self):
    #     assert self.browser.find_element(*BasePageLocators.LOGIN_LINK)

    # def test_should_be_add_to_basket(self):
    #     add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
    #     add_basket.click()
    #     print('first step')

    # def should_not_be_success_message(self):
    #    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #        "Success message is presented, but should not be"

    # def should_dissapear_of_success_message(self):
    #     assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"

    # def solve_quiz_and_get_code(self):
    #     alert = self.browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     alert.send_keys(answer)
    #     alert.accept()
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")
    #
    # def should_be_name_product(self):
    #     try:
    #         old = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_OLD).text
    #         new = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_NEW).text
    #         assert old == new
    #     except AssertionError:
    #         print("Name Problems")
    #     else:
    #         print("Done")
    #
    # def should_be_equally(self):
    #     try:
    #         price_name = self.browser.find_element(*ProductPageLocators.PRICE_NAME).text
    #         price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
    #         assert price_name == price_in_basket
    #     except AssertionError:
    #         print("Price not equally")
    #     else:
    #         print("Done")
