import logging
import allure
import time
import traceback

from playwright.async_api import Page, Error

LOGGER = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page, config):
        self.page = page
        self.config = config

    @allure.step("Handle the consent banner by clicking the 'Accept'")
    async def handle_consent_banner(self):
        """
        Handles the consent banner by clicking the 'Accept' button if it is present.
        This method attempts to locate and click the 'Accept' button on a consent
        banner that appears on the page. If the banner is not present.
        Exceptions:
        Error: Catches and ignores any Playwright errors that might occur if
        the button is not found or cannot be clicked.
        """
        try:
            await self.page.locator('button[aria-label="Consent"]').click()
            LOGGER.info("Consent banner clicked successfully.")
        except TimeoutError:
            LOGGER.error("Consent banner not found or not clickable.")
            raise Exception("Failed to click consent banner, test cannot proceed.")

    @allure.step("Assert current Page URL")
    async def assert_current_url(self, url: str, max_attempts=3):
        """
        Asserts that the current page URL matches the expected URL, with retries if the check fails.
        :param url: The expected URL to be verified.
        :param max_attempts: Maximum number of attempts to retry the assertion in case of a mismatch (default is 3).
        :raises AssertionError: If the actual URL does not match the expected URL after all attempts.
        :raises Exception: If there is an error during the retries or page loading.
        :return: None
        """
        for attempt in range(1, max_attempts + 1):
            try:
                current_url = self.page.url
                assert current_url == url, f"URL mismatch. Expected: {url}, Actual: {current_url}"
                LOGGER.info("URL checked")
                LOGGER.info("Successfully navigated to the Page. -> " + url)
                return
            except Exception as e:
                LOGGER.warning(f"URL checking failed on attempt {attempt}: {str(e)}")
                if attempt < max_attempts:
                    LOGGER.warning("Refreshing page and retrying...")
                    await self.page.reload()
                    await self.page.wait_for_load_state("load")
                    await self.page.goto(url)
                    await self.page.wait_for_load_state("load")
                else:
                    LOGGER.error(f"URL mismatch, after {max_attempts} attempts.")
                    raise

    @allure.step("Assert current Page title")
    async def assert_current_title(self, title: str):
        """
        Asserts that the current page title matches the expected title.
        :param title: The expected title of the current web page.
        :raises AssertionError: If the actual title does not match the expected title.
        :return: None
        """
        current_title = await self.page.title()
        assert current_title == title, f"Title mismatch. Expected: {title}, Actual: {current_title}"

    async def assert_url_and_title(self, expected_url: str, expected_title: str):
        """
        Asserts that the current URL and title match the expected values.
        :param expected_url: The expected URL to match.
        :param expected_title: The expected page title to match.
        """
        await self.assert_current_url(expected_url)
        await self.assert_current_title(expected_title)
