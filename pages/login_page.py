from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"
    # # URL = "https://practice.expandtesting.com/login"
    # URL = "https://demoqa.com/login"



    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    submit_button = (By.ID, "submit")
    error_message_locator = (By.ID, "error")

    # Methods
    def load(self):
        self.driver.get(self.URL)

    def enter_username(self, username: str):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_error_message(self) -> str:
        try:
            return self.driver.find_element(*self.error_message_locator).text
        except:
            return ""

    def get_current_url(self) -> str:
        return self.driver.current_url

    def is_logout_button_displayed(self) -> bool:
        try:
            return self.driver.find_element(By.LINK_TEXT, "Log out").is_displayed()
        
        except:
            return False

    def get_success_message(self) -> str:
        try:
            return self.driver.find_element(By.TAG_NAME, "h1").text
        except:
            return ""
