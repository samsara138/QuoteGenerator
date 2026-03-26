from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumBrowser:
    def __init__(self, url, headless=False):
        firefox_options = Options()
        firefox_options.add_argument('--ignore-certificate-errors')
        firefox_options.add_argument('--incognito')
        
        if headless:
            firefox_options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.get(url)

    def get_element_by_id(self, id, timeout=10):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(ec.visibility_of_element_located((By.ID, id)))
            return element
        except:
            print(f"ERROR: Cannot find element with id {id}")
            return None

    def get_element_by_xpath(self, xpath, timeout=10):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
            return element
        except:
            print(f"ERROR: Cannot find element with id {id}")
            return None

    def fill_input(self, element, input_string):
        element.send_keys(input_string)

    def click_button(self, button):
        button.click()

    def scroll_and_click_button(self, button):
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        ActionChains(self.driver).click(button).perform()


    def close(self):
        self.driver.quit()
