import logging
from pages.base_page import BasePage

LOGGER = logging.getLogger(__name__)


class LoginPage(BasePage):

    async def fill_signup(self, name: str, email: str):
        """
        Fills the signup form with the provided name and email address.
        :param name: The full name to be entered into the signup form.
        :param email: The email address to be entered into the signup form.
        :return: None
        """
        LOGGER.info("Enter name and email address")
        await self.page.locator(self.config["locators"]["login_page"]["signup"]["name_input"]).fill(name)
        await self.page.locator(self.config["locators"]["login_page"]["signup"]["email_input"]).fill(email)

    async def fill_login(self, email: str, password: str):
        """
        Fills the login form with the provided email address and password.
        :param email: The email address to be entered into the login form.
        :param password: The password to be entered into the login form.
        :return: None
        """
        LOGGER.info("Enter email and password")
        await self.page.locator(self.config["locators"]["login_page"]["login"]["email_input"]).fill(email)
        await self.page.locator(self.config["locators"]["login_page"]["login"]["password_input"]).fill(password)
