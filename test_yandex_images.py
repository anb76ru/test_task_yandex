import pytest
from conftest import browser
from pages.yandex_images_page import YandexImagePage

link = 'https://yandex.ru'

def test_should_be_yandex_search_page(browser):
    # Проверка на то, что открытая страница является страницей яндекса
    yandex_images_page = YandexImagePage(browser, link)
    yandex_images_page.open()
    yandex_images_page.should_be_yandex_search_page()

def test_should_be_link_to_images(browser):
    # Ссылка на картинки есть на странице
    yandex_images_page = YandexImagePage(browser, link)
    yandex_images_page.open()
    yandex_images_page.should_be_link_to_images()

def test_should_be_yandex_images_page(browser):
    # Проверка на переход на yandex.ru/images
    yandex_images_page = YandexImagePage(browser, link)
    yandex_images_page.open()
    yandex_images_page.should_be_yandex_images_page()

def test_should_be_open_first_category(browser):
    # Проверка что открылась первая категорияи текст в поиске совпадает с названием категории
    yandex_images_page = YandexImagePage(browser, link)
    yandex_images_page.open()
    yandex_images_page.should_be_open_first_category()

def test_should_be_open_first_image(browser):
    # Проверка открытия первой картинки
    yandex_images_page = YandexImagePage(browser, link)
    yandex_images_page.open()
    yandex_images_page.should_be_open_first_image()

def test_should_be_change_image_if_press_next_button(browser):
    # Проверка изменения картинки при нажатии "вперед"
    yandex_images_page = YandexImagePage(browser, link)
    yandex_images_page.open()
    yandex_images_page.should_be_change_image_if_press_next_button()

def test_should_be_first_image_if_press_prev_button(browser):
    # Проверка на то, что при нажатии "назад" открывается предыдущая картинка
    yandex_images_page = YandexImagePage(browser, link)
    yandex_images_page.open()
    yandex_images_page.should_be_first_image_if_press_prev_button()