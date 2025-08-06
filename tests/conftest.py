import pytest
from selenium import webdriver
from utils.logger import get_logger




logger = get_logger()

@pytest.fixture()
def driver():
    logger.info("Setting up Chrome WebDriver")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    logger.info("Quitting Chrome WebDriver")
    driver.quit()
