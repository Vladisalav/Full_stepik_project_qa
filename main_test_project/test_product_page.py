import time
from .pages.product_page import MainPage
import pytest


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.should_be_open_basket_from_product()
    time.sleep(5)
    page.should_be_clean()

# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#     page.should_be_open_basket()
#     time.sleep(5)
#     page.should_be_clean()


# def test_message_disappeared_after_adding_product_to_basket(browser):
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
# page.open()                      # открываем страницу
# page.should_be_login_page()
# page.test_should_be_add_to_basket()
# page.should_not_be_success_message()
# time.sleep(1)
# page.should_not_be_success_message()


# @pytest.mark.parametrize('number',
#                          [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
# def test_guest_can_add_product_to_basket(browser, number):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_login_page()
#     page.test_should_be_add_to_basket()
#     page.solve_quiz_and_get_code()
#     time.sleep(5)
#     page.should_be_name_product()
#     page.should_be_equally()
