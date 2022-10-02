from selenium import webdriver

class BasePage:
    def __init__(self, base_url="https://ya.ru/"):
        self.driver = webdriver.Chrome()
        self.base_url = base_url

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def quit_from_browser(self):
        return self.driver.quit()

    def get_driver(self):
        return self.driver
