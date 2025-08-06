import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.parametrize("username,password,expected_url,expected_msg,expect_logout", [
    ("student", "Password123", "practicetestautomation.com/logged-in-successfully/", "Logged In Successfully", True),   # Positive test
    # ("practice", "SuperSecretPassword!", "https://practice.expandtesting.com/secure", "Your username is invalid!", True),                                    # Negative username
    # ("ryadav", "Rajat@123456", "https://demoqa.com/profile", "Your password is invalid!", True),                                    # Negative password
])
def test_login(driver, username, password, expected_url, expected_msg, expect_logout):
    login_page = LoginPage(driver)
    login_page.load()
    # driver.implicitly_wait(15)
    logger.info(f"Testing login with username: {username} and password: {password}")
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.submit()
    print("------------@@@@@@@@@@@@@@@@@@@@@@-------------",login_page.get_success_message())




    if expected_url:
        assert expected_url in login_page.get_current_url()
        assert expected_msg in login_page.get_success_message()
        assert login_page.is_logout_button_displayed() == expect_logout
        logger.info("Login successful and logout button found.")
    else:
        error_msg = login_page.get_error_message()
        assert expected_msg == error_msg
        logger.info(f"Expected error message displayed: {error_msg}")
