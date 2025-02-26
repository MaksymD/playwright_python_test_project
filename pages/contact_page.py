import logging
import allure
from pages.base_page import BasePage

LOGGER = logging.getLogger(__name__)


class ContactPage(BasePage):

    @allure.step("Filling the contact form with the required details")
    async def fill_contact_form(self):
        """
        Fills the contact form with the required details including name, email, subject, message,
        and file upload. The data for the form fields are fetched from the configuration (`self.config`)
        that holds locators and test data.
        :raises Exception: If any of the elements are not found or an error occurs during interaction with the page.
        :return: None
        """
        LOGGER.info("Fill details: Name, Email, Subject, Massage")
        await self.page.locator(self.config["locators"]["contact_page"]["name_input"]).fill(
            self.config["testData"]["contact_form"]["full_name"])
        await self.page.locator(self.config["locators"]["contact_page"]["email_input"]).fill(
            self.config["testData"]["contact_form"]["email"])
        await self.page.locator(self.config["locators"]["contact_page"]["subject_input"]).fill(
            self.config["testData"]["contact_form"]["subject"])
        await self.page.locator(self.config["locators"]["contact_page"]["message_textarea"]).fill(
            self.config["testData"]["contact_form"]["message"])
        LOGGER.info("Select file to upload")
        await self.page.locator(self.config["locators"]["contact_page"]["file_input"]).set_input_files(
            "./data/upload_files/test_file.txt")
        LOGGER.info("Setting up dialog handler")
        self.page.once("dialog", lambda dialog: dialog.accept())
        LOGGER.info("Click 'Submit' button")
        await self.page.locator(self.config["locators"]["contact_page"]["submit_button"]).click()
