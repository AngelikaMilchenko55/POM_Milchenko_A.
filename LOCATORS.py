from selenium.webdriver.common.by import By

class Locators:
    search_field = (By.ID, "text")
    search_button = (By.CLASS_NAME, "search3__button.mini-suggest__button")
    clear_button = (By.CLASS_NAME, "search3__svg_clear")
    element_nav_bar1 = (By.LINK_TEXT, "Картинки")

    keyboard_button = (By.CLASS_NAME, "search3__svg_keyboard")
    keyboard_letter = (By.CLASS_NAME, "keyboard__key-m")