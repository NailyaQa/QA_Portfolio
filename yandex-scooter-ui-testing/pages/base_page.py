from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait_for_visible(locator)
        return element.text
    
    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )
        return element
    
    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        element = self.scroll_to_element(locator)
        element.click()

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

    def wait_and_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
        element.click()

    def scroll_and_click(self, locator):
        element = self.driver.find_element(*locator)

        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
            element
    )

        element.click()

    @allure.step("Ввести текст")
    def fill_input(self, locator, text):
        self.wait_for_visible(locator).send_keys(text)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Дождаться открытия новой вкладки")
    def wait_for_new_tab(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        lambda d: len(d.window_handles) > 1
    )
    @allure.step("Переключиться на последнюю вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(
        self.driver.window_handles[-1]
    )
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Дождаться открытия страницы по URL")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        lambda d: text in d.current_url
    )