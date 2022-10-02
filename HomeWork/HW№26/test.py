import pytest
from init import YandexSearcher
import time

@pytest.fixture()
def yandex_page():
    return YandexSearcher()

@pytest.fixture()
def browser(yandex_page):
    yandex_page.go_to_site()
    yield
    yandex_page.quit_from_browser()

def test_search(yandex_page, browser):
    yandex_page.enter_word("cat")
    yandex_page.click_on_the_search_button()
    time.sleep(2)

def test_enter_in_field_and_clear_words(yandex_page, browser):
    yandex_page.enter_word("cat")
    time.sleep(2)
    yandex_page.click_on_the_clear_button()
    yandex_page.enter_word("dog")
    yandex_page.click_on_the_search_button()
    time.sleep(2)

def test_yandex_search_nav(yandex_page, browser):
    yandex_page.enter_word("cat")
    yandex_page.click_on_the_search_button()
    time.sleep(2)
    yandex_page.click_on_the_nav()
    time.sleep(2)

def test_yandex_search_button_keyboard(yandex_page, browser):
    yandex_page.enter_word("")
    yandex_page.click_on_the_keyboard_button()
    time.sleep(2)
    elements = yandex_page.find_letter_on_the_keyboard()
    for i in range(1, 5):
        elements[i].click()
    time.sleep(1)
    yandex_page.click_on_the_search_button()
    time.sleep(2)
