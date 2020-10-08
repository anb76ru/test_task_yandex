import pytest
from selenium import webdriver
from conftest import browser
from pages.yandex_search_page import YandexSearchPage

link = 'http://yandex.ru'

def test_should_be_yandex_page(browser):
    # Проверка на то, что открытая страница является страницей яндекса
    yandex_search_page = YandexSearchPage(browser, link)
    yandex_search_page.open()
    yandex_search_page.should_be_yandex_search_page()

def test_shoul_be_search_field(browser):
    # Проверка на наличие поля поиска
    yandex_search_page = YandexSearchPage(browser, link)
    yandex_search_page.open()
    yandex_search_page.should_be_search_field()

def test_should_be_suggest(browser):
    # Проверка на наличие всплывающей таблицы с подсказками
    yandex_search_page = YandexSearchPage(browser, link)
    yandex_search_page.open()
    yandex_search_page.should_be_suggest()

def test_should_be_search_result_table(browser):
    # Проверка на наличие результатов поиска при нажатии Enter
    yandex_search_page = YandexSearchPage(browser, link)
    yandex_search_page.open()
    yandex_search_page.should_be_search_result_table()

def test_should_be_tensor_website(browser):
    # Проверка на то, что в первых пяти результатах поиска есть ссылка на tensor.ru
    yandex_search_page = YandexSearchPage(browser, link)
    yandex_search_page.open()
    yandex_search_page.should_be_tensor_website()