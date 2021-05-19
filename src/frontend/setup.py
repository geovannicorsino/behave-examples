import pyderman

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_browser(context):
    if "skip" not in context.scenario.effective_tags:
        path = pyderman.install(browser=pyderman.chrome, file_directory='./drivers')
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
        driver.maximize_window()
        driver.implicitly_wait(time_to_wait=10)
        return driver
    else:
        return None
