from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains





class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click_element(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url
    
    
    def drag_and_drop(self, source_locator, target_locator):

        source = self.find_element(source_locator)
        target = self.find_present_element(target_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            source
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            target
        )
        

        ActionChains(self.driver) \
            .move_to_element(source) \
            .pause(1) \
            .click_and_hold() \
            .pause(1) \
            .move_to_element(target) \
            .pause(2) \
            .release() \
            .perform()
        
            
        

       
    


    def find_present_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def click_element_by_js(self, locator):

        element = self.find_element(locator)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

   

   


    def drag_and_drop_js(
        self,
        source_locator,
        target_locator
):
        source = self.find_element(source_locator)
        target = self.find_present_element(target_locator)

        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            source.dispatchEvent(
                new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );

            target.dispatchEvent(
                new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );

            target.dispatchEvent(
                new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );

            source.dispatchEvent(
                new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );
            """,
            source,
            target
        )

    def remove_modal(self):
        self.driver.execute_script(
            """
            document.querySelectorAll(
                '[class*="Modal_modal_overlay"]'
            ).forEach(element => element.remove());

            document.querySelectorAll(
                '[class*="Modal_modal"]'
            ).forEach(element => element.remove());

            document.body.style.overflow = 'auto';
            """
        )

    def wait_for_invisibility(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator)
        )


    
    