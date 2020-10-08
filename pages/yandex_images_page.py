from .yandex_page import YandexPage
from .locators import YandexImagesLocators
from selenium.common.exceptions import NoSuchElementException


class YandexImagePage(YandexPage):
    def should_be_yandex_search_page(self):
        # сравнение адреса открытой страницы с yandex.ru
        assert 'https://yandex.ru/' == self.browser.current_url, 'Current page is not "yandex.ru"'

    def should_be_link_to_images(self):
        # Ссылка на картинки есть на странице
        assert self.is_element_present(*YandexImagesLocators.IMAGES_LINK), 'Link "Images" is not present'

    def should_be_yandex_images_page(self):
        # Открытая страница является страницей с картинками
        self.go_to_images_page()
        assert 'https://yandex.ru/images/' in self.browser.current_url
    
    def should_be_open_first_category(self):
        # Должна открываться первая категория
        """ Критерий открытия страницы следующий:
            1) скрипт 'return document.readyState' возвращает значение 'complete'
            2) количество элементов с картинками на странице не нулевое
        
        """
        self.go_to_images_page()

        first_category_name = self.browser.find_element(*YandexImagesLocators.FIRST_CATEGORY_NAME)
        category_name_text = first_category_name.text

        frirst_category = self.browser.find_element(*YandexImagesLocators.FIRST_CATEGORY)
        frirst_category.click()

        text_in_search_field = self.browser.find_element(*YandexImagesLocators.TEXT_IN_SEARCH_FIELD)
        loading_status = self.browser.execute_script("return document.readyState")
        
        assert (loading_status == 'complete' 
                and len(self.browser.find_elements(*YandexImagesLocators.IMAGES)) > 0 
                and category_name_text == text_in_search_field.get_attribute('value')), '''Page 
        is not loading or text in search field not equal category name
        
        '''
    
    def should_be_open_first_image(self):
        # функция открывает первую картинку, проверяется что открылась
        self.go_to_images_page()
        self.open_first_image()
        assert self.is_element_present(*YandexImagesLocators.CURRENT_IMAGE_OPENED), 'Image is not open'
    
    def should_be_change_image_if_press_next_button(self):
        # картинка меняется, если нажать "вперед"
        self.go_to_images_page()
        self.open_first_image()

        first_image_src = self.get_src_current_image()
        circle_button_next = self.browser.find_element(*YandexImagesLocators.CIRCLE_BUTTON_NEXT)
        circle_button_next.click()

        next_picture_src = self.get_src_current_image()

        assert first_image_src != next_picture_src, 'Images is not different'


    def should_be_first_image_if_press_prev_button(self):
        # при нажатии "назад" открывается предыдущая картинка
        self.go_to_images_page()
        self.open_first_image()

        first_image_src = self.get_src_current_image()
        circle_button_next = self.browser.find_element(*YandexImagesLocators.CIRCLE_BUTTON_NEXT)
        circle_button_next.click()

        circle_button_prev = self.browser.find_element(*YandexImagesLocators.CIRCLE_BUTTON_PREV)
        circle_button_prev.click()

        current_picture_src = self.get_src_current_image()
        assert current_picture_src == first_image_src, 'Image is different'

    

    def go_to_images_page(self):
        # функция перехода на страницу с картинками
        link_to_images_page = self.browser.find_element(*YandexImagesLocators.IMAGES_LINK)
        link_to_images_page.click()
        images_page = self.browser.window_handles[1]
        self.browser.switch_to.window(images_page)

    def open_first_image(self):
        # Открытие первой картинки
        frirst_category = self.browser.find_element(*YandexImagesLocators.FIRST_CATEGORY)
        frirst_category.click()
        first_image = self.browser.find_element(*YandexImagesLocators.FIRST_IMAGE)
        first_image.click()

    def get_src_current_image(self):
        # Функция получает ссылку на источник картинки
        current_image = self.browser.find_element(*YandexImagesLocators.CURRENT_IMAGE_OPENED)
        return current_image.get_attribute('src')
    
