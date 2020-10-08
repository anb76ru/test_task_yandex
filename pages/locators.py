from selenium.webdriver.common.by import By

class YandexSearchPageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, '.input .mini-suggest__input')
    SUGGEST = (By.CSS_SELECTOR, 'div.mini-suggest__popup')
    SEARCH_RESULT = (By.ID, 'search-result')
    LIST_LINK = (By.CSS_SELECTOR, "a > b")


class YandexImagesLocators():
    IMAGES_LINK = (By.XPATH, '//a[@data-id = "images"]')
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    FIRST_CATEGORY_NAME = (By.CSS_SELECTOR, 'a .PopularRequestList-SearchText')
    IMAGES = (By.CSS_SELECTOR, '.serp-item_group_search')
    TEXT_IN_SEARCH_FIELD = (By.CSS_SELECTOR, 'span > .input__control')
    FIRST_IMAGE = (By.CSS_SELECTOR, 'a.serp-item__link')
    CURRENT_IMAGE_OPENED = (By.CSS_SELECTOR, '.MMImage-Preview')
    CIRCLE_BUTTON_NEXT = (By.CSS_SELECTOR, '.CircleButton_type_next')
    CIRCLE_BUTTON_PREV = (By.CSS_SELECTOR, '.CircleButton_type_prev')