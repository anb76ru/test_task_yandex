import requests
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys

from .yandex_page import YandexPage
from .locators import YandexSearchPageLocators


class YandexSearchPage(YandexPage):
    def should_be_yandex_search_page(self):
        # сравнение адреса открытой страницы с yandex.ru
        assert 'https://yandex.ru/' == self.browser.current_url, 'Current page is not "yandex.ru"'

    def should_be_search_field(self):
        # ищем строку поиска
        assert self.is_element_present(*YandexSearchPageLocators.SEARCH_FIELD), 'Search field not found'
    
    def should_be_suggest(self):
        # поиск  всплывающей подсказки
        self.input_text_in_search_field()
        assert self.is_element_present(*YandexSearchPageLocators.SUGGEST), 'Suggest table is not present'

    def should_be_search_result_table(self):
        # наличие результатов поиска на странице
        search_field = self.input_text_in_search_field()
        search_field.send_keys(Keys.ENTER)
        assert self.browser.find_elements(*YandexSearchPageLocators.SEARCH_RESULT)

    def should_be_tensor_website(self):
        # перебор первых пяти результатов поиска
        search_field = self.input_text_in_search_field()
        search_field.send_keys(Keys.ENTER)
        
        list_link = self.get_content()
        flag = False
        for href in list_link:
            if 'tensor.ru' in href.get('href'):
                flag = True
                break
        assert flag == True, 'Website "tensor.ru" is not present in the first five links'

    def input_text_in_search_field(self):
        # функция ввода текста в поле поиска
        search_field = self.browser.find_element(*YandexSearchPageLocators.SEARCH_FIELD)
        search_field.send_keys('Тензор')
        return search_field

    def get_content(self):
        # получение первых пяти результатов поиска
        list_link = []
        current_url = self.browser.current_url
        html = requests.get(current_url)
        soup = BeautifulSoup(html.text, 'html.parser')
        links = soup.find_all('a', class_ = 'link link_theme_outer path__item i-bem')
        for link in links:
            list_link.append(link)
        return list_link[0:5]