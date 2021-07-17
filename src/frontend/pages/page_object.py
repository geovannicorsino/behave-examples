import logging

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located


class PageObjectModel:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get()

    def wait(self, expec_conditions, selector):
        try:
            WebDriverWait(self.driver, 3).until(expec_conditions)
            element = self.driver.find_element(*selector)
            self.move_to_element(element)
            original_style = element.get_attribute('style')
            self.__apply_style(self.driver, element)
            return element, original_style
        except TimeoutException:
            logging.exception(f'Timeout Exception on trying to find the element: {selector}')
            assert False
        except WebDriverException:
            logging.exception(f'Unable to locate element: {selector}')
            assert False

    def click(self, selector):
        element, original_style = self.wait(element_to_be_clickable(selector), selector)
        element.click()

    def select(self, selector, item):
        element, original_style = self.wait(element_to_be_clickable(selector), selector)
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            option.get_attribute(item)
            option.click()

    def send_keys(self, keys, selector):
        element, original_style = self.wait(visibility_of_element_located(selector), selector)
        element.send_keys(keys)
        self.__apply_style(element, original_style)

    def text(self, selector):
        element, original_style = self.wait(visibility_of_element_located(selector), selector)
        self.__apply_style(element, original_style)
        return element.text

    def is_visible(self, selector):
        try:
            if self.driver.find_element(*selector).is_displayed():
                return True
            else:
                return False
        except TimeoutException:
            logging.exception(f'Timeout Exception on trying to find the element: {selector}')
            assert False
        except WebDriverException:
            logging.exception(f'Unable to locate element: {selector}')
            assert False

    def elements_list(self, selector):
        try:
            WebDriverWait(self.driver, 3).until(presence_of_all_elements_located(selector))
            return self.driver.find_elements(selector)
        except TimeoutException:
            logging.exception(f'Timeout Exception on trying to find the element: {selector}')
            assert False
        except WebDriverException:
            logging.exception(f'Unable to locate element: {selector}')
            assert False

    def see(self, selector):
        element, original_style = self.wait(visibility_of_element_located(selector), selector)
        self.__apply_style(element, original_style)

    def mouse_hover(self, selector):
        element = self.driver.find_element(*selector)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def move_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def __apply_style(self, element, style="border: {0}px solid {1};".format(5, "red")):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)
