import logging
import allure
from pages.base_page import BasePage

LOGGER = logging.getLogger(__name__)


class SignupPage(BasePage):

    @allure.step("Filling the signup form with the required details")
    async def fill_signup_form(self):
        """
        Fills the signup form with the required details including title, name, email, password,
        date of birth, newsletter preference, special offers checkbox, and address information.
        The data for the form fields are fetched from the configuration (`self.config`) that holds
        locators and test data.
        :raises Exception: If any of the elements are not found or an error occurs during interaction with the page.
        :return: None
        """
        LOGGER.info("Fill details: Title, Name, Email, Password, Date of birth")
        await self.page.locator(self.config["locators"]["signup_page"]["mr_radio"]).click()
        await self.page.locator(self.config["locators"]["signup_page"]["name_input"]).fill(
            self.config["testData"]["signup_form"]["full_name"])
        await self.page.locator(self.config["locators"]["signup_page"]["password_input"]).fill(
            self.config["testData"]["signup_form"]["password"])
        await self.page.locator(self.config["locators"]["signup_page"]["day_select"]).select_option(value="1")
        await self.page.locator(self.config["locators"]["signup_page"]["month_select"]).select_option(value="1")
        await self.page.locator(self.config["locators"]["signup_page"]["year_select"]).select_option(value="1980")
        LOGGER.info("Select checkbox 'Sign up for our newsletter!'")
        await self.page.locator(self.config["locators"]["signup_page"]["newsletter_checkbox"]).check()
        LOGGER.info("Select checkbox 'Receive special offers from our partners!'")
        await self.page.locator(self.config["locators"]["signup_page"]["offer_checkbox"]).check()
        LOGGER.info("Fill details: First name, Last name, Company, Address, Country, State, City, PLZ, Mobile Number")
        await self.page.locator(self.config["locators"]["signup_page"]["firstName_input"]).fill(
            self.config["testData"]["signup_form"]["first_name"])
        await self.page.locator(self.config["locators"]["signup_page"]["lastName_input"]).fill(
            self.config["testData"]["signup_form"]["last_name"])
        await self.page.locator(self.config["locators"]["signup_page"]["company_input"]).fill(
            self.config["testData"]["signup_form"]["company"])
        await self.page.locator(self.config["locators"]["signup_page"]["address_input"]).fill(
            self.config["testData"]["signup_form"]["address_street"])
        await self.page.locator(self.config["locators"]["signup_page"]["address2_input"]).fill(
            self.config["testData"]["signup_form"]["address_street"])
        await self.page.locator(self.config["locators"]["signup_page"]["country_select"]).select_option(value="Canada")
        await self.page.locator(self.config["locators"]["signup_page"]["state_input"]).fill(
            self.config["testData"]["signup_form"]["address_country"])
        await self.page.locator(self.config["locators"]["signup_page"]["city_input"]).fill(
            self.config["testData"]["signup_form"]["address_country"])
        await self.page.locator(self.config["locators"]["signup_page"]["zipcode_input"]).fill(
            str(self.config["testData"]["signup_form"]["address_plz"]))
        await self.page.locator(self.config["locators"]["signup_page"]["mobile_input"]).fill(
            str(self.config["testData"]["signup_form"]["phone"]))
