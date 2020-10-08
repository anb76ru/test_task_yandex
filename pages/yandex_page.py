from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class YandexPage():
    # Определим базовый класс дял страницы яндекса
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        # открытие нужной страницы
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # Метод для перехвата исключений.  Проверяет наличие элемента на cтранице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True