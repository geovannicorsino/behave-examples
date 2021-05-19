import logging
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located


def apply_style(context, element, style="border: {0}px solid {1};".format(5, "red")):
    context.browser.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)


def wait(context, expec_conditions, selector):
    try:
        WebDriverWait(context.browser, 3).until(expec_conditions)
        element = context.browser.find_element(*selector)
        move_to_element(context, element)
        original_style = element.get_attribute('style')
        # take_screenshot(context)
        apply_style(context, element)
        # take_screenshot(context)
        return element, original_style
    except WebDriverException:
        logging.exception((f'Unable to locate element: {selector}'))
        assert False
    except TimeoutException:
        logging.exception(f'Timeout Exception on trying to find the element: {selector}')
        assert False


def click(context, selector):
    element, original_style = wait(context, element_to_be_clickable(selector), selector)
    element.click()
    # take_screenshot(context)


def send_keys(context, keys, selector):
    element, original_style = wait(context, visibility_of_element_located(selector), selector)
    element.send_keys(keys)
    # take_screenshot(context)
    apply_style(context, element, original_style)


def text(context, selector):
    element, original_style = wait(context, visibility_of_element_located(selector), selector)
    apply_style(context, element, original_style)
    return element.text


def is_visible(context, selector):
    try:
        if context.browser.find_element(*selector).is_displayed():
            return True
        else:
            return False
    except WebDriverException:
        logging.exception(context, f'Unable to locate element: {selector}')
        assert False
    except TimeoutException:
        logging.exception(context, f'Timeout Exception on trying to find the element: {selector}')
        assert False


def elements_list(context, selector):
    try:
        WebDriverWait(context.browser, 3).until(presence_of_all_elements_located(selector))
        return context.browser.find_elements(selector)
    except WebDriverException:
        logging.exception(f'Unable to locate element: {selector}')
        assert False
    except TimeoutException:
        logging.exception(f'Timeout Exception on trying to find the element: {selector}')
        assert False


def see(context, selector):
    element, original_style = wait(context, visibility_of_element_located(selector), selector)
    apply_style(context, element, original_style)


def mouse_hover(context, selector):
    element = context.browser.find_element(*selector)
    hover = ActionChains(context.browser).move_to_element(element)
    hover.perform()
    # take_screenshot(context)


def move_to_element(context, element):
    context.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                                   element)
