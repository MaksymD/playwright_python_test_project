import os
import allure
import pytest
from fixtures.conftest import page_with_playwright_async, LOGGER
from pages.base_page import BasePage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.config_manager import ConfigurationManager

config_manager = ConfigurationManager()


@allure.step("Navigate to the main URL")
async def navigate_to_main(page, config):
    base_page = BasePage(page, config)
    LOGGER.info("Navigating to main URL")
    await page.goto(config["urls"]["main_url"])
    await base_page.handle_consent_banner()
    await base_page.assert_url_and_title(config["urls"]["main_url"], config["page_title"]["main"])


@allure.step("Click on 'Signup / Login' button")
async def click_signup_login_in_navigation_menu(page, config):
    base_page = BasePage(page, config)
    LOGGER.info("Click on 'Signup / Login' button")
    await page.locator(config["locators"]["navbar"]["login_button"]).click()
    await base_page.assert_url_and_title(config["urls"]["login_url"], config["page_title"]["signup_login"])


@allure.step("Click on 'Contact Us' button")
async def click_contact_us_in_navigation_menu(page, config):
    base_page = BasePage(page, config)
    LOGGER.info("Click on 'Contact Us' button")
    await page.locator(config["locators"]["navbar"]["contact_button"]).click()
    await base_page.assert_url_and_title(config["urls"]["contact_url"], config["page_title"]["contact"])


@allure.step("Click on 'Home' button")
async def click_home_in_navigation_menu(page, config):
    base_page = BasePage(page, config)
    LOGGER.info("Click on 'Home' button")
    await page.locator(config["locators"]["navbar"]["home_button"]).click()
    await base_page.assert_url_and_title(config["urls"]["main_url"], config["page_title"]["main"])


@allure.step("Complete contact us form and clicking 'Submit' button")
async def complete_contact_form(page, config):
    LOGGER.info("Verifying 'GET IN TOUCH' message is visible")
    assert await page.locator(config["locators"]["contact_page"]["title_contactForm"]).is_visible(), \
        "Form title 'GET IN TOUCH' not visible"
    contact_page = ContactPage(page, config)
    LOGGER.info("Filling contact form")
    await contact_page.fill_contact_form()


@allure.step("Verify success message 'Success! Your details have been submitted successfully.' is visible")
async def verify_contact_form_send(page, config):
    base_page = BasePage(page, config)
    LOGGER.info("Verifying 'Success!...' message is visible")
    assert await page.locator(config["locators"]["contact_page"]["text_send_success"]).is_visible(), \
        "Form text 'Success!...' message not visible"
    LOGGER.info("Clicking 'Home' button")
    await page.locator(config["locators"]["contact_page"]["home_button"]).click()
    await base_page.assert_url_and_title(config["urls"]["main_url"], config["page_title"]["main"])


@allure.step("Login with correct email and password")
async def login(page, config):
    login_page = LoginPage(page, config)
    LOGGER.info("Entering correct email and password")
    await login_page.fill_login(config["user_credentials"]["test_username"],
                                config["user_credentials"]["test_password"])
    LOGGER.info("Click 'Login' button")
    await page.locator(config["locators"]["login_page"]["login"]["login_button"]).click()


@allure.step("Enter name and email for registration")
async def signup(page, config):
    login_page = LoginPage(page, config)
    LOGGER.info("Entering name and email for signup")
    await login_page.fill_signup(config["testData"]["signup_form"]["full_name"],
                                 config["testData"]["signup_form"]["email"])
    LOGGER.info("Clicking 'Signup' button")
    await page.locator(config["locators"]["login_page"]["signup"]["signup_button"]).click()


@allure.step("Complete signup form and clicking 'Create Account' button")
async def complete_signup_form(page, config):
    signup_page = SignupPage(page, config)
    LOGGER.info("Filling signup form")
    await signup_page.fill_signup_form()
    LOGGER.info("Clicking 'Create Account' button")
    await page.locator(config["locators"]["signup_page"]["submit_button"]).click()


@allure.step("Verify that 'Logged in as username' is visible")
async def verify_logged_user(page, config):
    base_page = BasePage(page, config)
    try:
        await base_page.assert_url_and_title(config["urls"]["main_url"], config["page_title"]["main"])
        LOGGER.info(f"Verify that 'Logged in as {config['user_credentials']['test_username']}' is visible")
        assert await page.locator(config["locators"]["main_page"]["user_name"]).is_visible(), \
            "Failed to verify 'Logged in as username'"
    except Exception as e:
        LOGGER.error(f"Error verifying logged in user: {str(e)}")
        raise


@allure.step("Verify 'Account Created' is visible")
async def verify_account_created(page, config):
    base_page = BasePage(page, config)
    await base_page.assert_current_url(config["urls"]["create_account_url"])
    LOGGER.info("Verifying 'ACCOUNT CREATED!' message is visible")
    assert await page.locator(config["locators"]["create_account_page"]["title_created"]).is_visible(), \
        "Account Creation confirmation not visible"
    LOGGER.info("Clicking 'Continue' button after account creation")
    await page.locator(config["locators"]["create_account_page"]["continue_button"]).click()


@allure.step("Click 'Delete Account' button")
async def click_delete_account(page, config):
    LOGGER.info("Clicking 'Delete Account' button in navigation menu")
    await page.locator(config["locators"]["navbar"]["delete_button"]).click()


@allure.step("Verify 'Account Deleted' is visible")
async def verify_account_deleted(page, config):
    base_page = BasePage(page, config)
    await base_page.assert_current_url(config["urls"]["delete_account_url"])
    LOGGER.info("Verifying 'ACCOUNT DELETED!' message is visible")
    assert await page.locator(config["locators"]["delete_account_page"]["title_deleted"]).is_visible(), \
        "Account Deletion confirmation not visible"
    LOGGER.info("Clicking 'Continue' button after account deletion")
    await page.locator(config["locators"]["create_account_page"]["continue_button"]).click()


@allure.step("Attach video to Allure report")
def attach_video_to_allure(video_path, test_name):
    with open(video_path, 'rb') as video_file:
        allure.attach(video_file.read(), name=f"{test_name} Video", attachment_type=allure.attachment_type.MP4)


@allure.parent_suite("UI tests")
@allure.suite("User - Signup/Login")
@allure.tag("UI Test")
@allure.title("Test Case 1: Register User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Signup / Login' button
            5. Verify 'New User Signup!' is visible
            6. Enter name and email address
            7. Click 'Signup' button
            8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
            9. Fill details: Title, Name, Email, Password, Date of birth
            10. Select checkbox 'Sign up for our newsletter!'
            11. Select checkbox 'Receive special offers from our partners!'
            12. Fill details: First name, Last name, Company, Address, 
            Address2, Country, State, City, Zipcode, Mobile Number
            13. Click 'Create Account button'
            14. Verify that 'ACCOUNT CREATED!' is visible
            15. Click 'Continue' button
            16. Verify that 'Logged in as username' is visible""")
@pytest.mark.asyncio
@pytest.mark.only_browser("chromium")
@pytest.mark.order(1)
async def test_registration_success(page_with_playwright_async, request):
    async for page, config in page_with_playwright_async:
        # Step 1: Navigate to the main URL
        await navigate_to_main(page, config)

        # Step 2: Click on 'Signup / Login' button
        await click_signup_login_in_navigation_menu(page, config)

        # Step 3: Enter name and email for registration
        await signup(page, config)

        # Step 4: Complete signup form
        await complete_signup_form(page, config)

        # Step 5: Verify 'Account Created' is visible
        await verify_account_created(page, config)

        # Step 6: Verify that 'Logged in as username' is visible
        await verify_logged_user(page, config)

        # attach video to the Allure report
        video_path = await page.video.path()
        if video_path and os.path.exists(video_path):
            test_name = request.node.name
            attach_video_to_allure(video_path, test_name)


@allure.parent_suite("UI tests")
@allure.suite("User - Signup/Login")
@allure.tag("UI Test")
@allure.title("Test Case 2: Login User with correct email and password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Signup / Login' button
            5. Verify 'Login to your account' is visible
            6. Enter correct email address and password
            7. Click 'login' button
            8. Verify that 'Logged in as username' is visible""")
@pytest.mark.asyncio
@pytest.mark.only_browser("chromium")
@pytest.mark.order(2)
async def test_login_user_with_correct_email_and_password(page_with_playwright_async, request):
    async for page, config in page_with_playwright_async:
        # Step 1: Navigate to the main URL
        await navigate_to_main(page, config)

        # Step 2: Click on 'Signup / Login' button
        await click_signup_login_in_navigation_menu(page, config)

        # Step 3: Login with correct email and password
        await login(page, config)

        # Step 4: Verify that 'Logged in as username' is visible
        await verify_logged_user(page, config)

        # attach video to the Allure report
        video_path = await page.video.path()
        if video_path and os.path.exists(video_path):
            test_name = request.node.name
            attach_video_to_allure(video_path, test_name)


@allure.parent_suite("UI tests")
@allure.suite("User - Signup/Login")
@allure.tag("UI Test")
@allure.title("Test Case 3: Delete account")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Signup / Login' button
            5. Verify 'Login to your account' is visible
            6. Enter correct email address and password
            7. Click 'login' button
            8. Verify that 'Logged in as username' is visible
            9. Click 'Delete Account' button
            10. Verify that 'ACCOUNT DELETED!' is visible""")
@pytest.mark.asyncio
@pytest.mark.only_browser("chromium")
@pytest.mark.order(3)
async def test_delete_account(page_with_playwright_async, request):
    async for page, config in page_with_playwright_async:
        # Step 1: Navigate to the main URL
        await navigate_to_main(page, config)

        # Step 2: Click on 'Signup / Login' button
        await click_signup_login_in_navigation_menu(page, config)

        # Step 3: Login with correct email and password
        await login(page, config)

        # Step 4: Verify that 'Logged in as username' is visible
        await verify_logged_user(page, config)

        # Step 5: Click 'Delete Account' button
        await click_delete_account(page, config)

        # Step 6: Verify 'Account Deleted' is visible
        await verify_account_deleted(page, config)

        # attach video to the Allure report
        video_path = await page.video.path()
        if video_path and os.path.exists(video_path):
            test_name = request.node.name
            attach_video_to_allure(video_path, test_name)


@allure.parent_suite("UI tests")
@allure.suite("Contact Form")
@allure.tag("UI Test")
@allure.title("Test Case 1: Contact Us Form")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
            1. Launch browser
            2. Navigate to url 'http://automationexercise.com'
            3. Verify that home page is visible successfully
            4. Click on 'Contact Us' button
            5. Verify 'GET IN TOUCH' is visible
            6. Enter name, email, subject and message
            7. Upload file
            8. Click 'Submit' button
            9. Click OK button
            10. Verify success message 'Success! Your details have been submitted successfully.' is visible
            11. Click 'Home' button and verify that landed to home page successfully""")
@pytest.mark.asyncio
@pytest.mark.only_browser("chromium")
@pytest.mark.order(4)
async def test_contact_form(page_with_playwright_async, request):
    async for page, config in page_with_playwright_async:
        # Step 1: Navigate to the main URL
        await navigate_to_main(page, config)

        # Step 2: Click on 'Contact Us' button
        await click_contact_us_in_navigation_menu(page, config)

        # Step 3: Complete contact form
        await complete_contact_form(page, config)

        # Step 4: Verify success message after sending contact form
        await verify_contact_form_send(page, config)

        # Step 5: Verify that landed to home page successfully
        await click_home_in_navigation_menu(page, config)

        # attach video to the Allure report
        video_path = await page.video.path()
        if video_path and os.path.exists(video_path):
            test_name = request.node.name
            attach_video_to_allure(video_path, test_name)
