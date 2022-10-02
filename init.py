from basePage import BasePage
from LOCATORS import Locators

class YandexSearcher(BasePage):
    def enter_word(self, word):
        search_field = self.driver.find_element(Locators.search_field[0], Locators.search_field[1])
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        search_button = self.driver.find_element(Locators.search_button[0], Locators.search_button[1])
        search_button.click()
        return search_button

    def click_on_the_clear_button(self):
        clear_button = self.driver.find_element(Locators.clear_button[0], Locators.clear_button[1])
        clear_button.click()
        return clear_button

    def click_on_the_nav(self):
        search_button_nav = self.driver.find_element(Locators.element_nav_bar1[0], Locators.element_nav_bar1[1])
        search_button_nav.click()
        return search_button_nav

    def find_element_in_nav_bar(self):
        list_elements = self.driver.find_elements(Locators.element_nav_bar[0], Locators.element_nav_bar[1])
        return list_elements

    def click_on_the_keyboard_button(self):
        search_button_keyboard = self.driver.find_element(Locators.keyboard_button[0], Locators.keyboard_button[1])
        search_button_keyboard.click()
        return search_button_keyboard

    def find_letter_on_the_keyboard(self):
        letter_elements = self.driver.find_elements(Locators.keyboard_letter[0], Locators.keyboard_letter[1])
        return letter_elements