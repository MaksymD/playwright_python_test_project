import logging
import os
import allure
import shutil
import pytest
from playwright.async_api import async_playwright
from utils.config_manager import ConfigurationManager

LOGGER = logging.getLogger(__name__)


async def handle_console_messages(page):
    def console_filter(msg):
        # Ignore 'Mixed Content' warnings. Only for this test website
        if 'Mixed Content' in msg.text:
            return
        LOGGER.info(f"Console [{msg.type}]: {msg.text}")

    page.on("console", console_filter)


@pytest.fixture(autouse=True)
def clean_allure_results():
    allure_results_dir = './allure-results'
    if os.path.exists(allure_results_dir):
        LOGGER.info(f"Removing existing Allure results directory: {allure_results_dir}")
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir)


@pytest.fixture(scope="function")
@allure.title("Prepare for the test")
async def page_with_playwright_async(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--start-maximized"],
            channel="chrome",
        )
        context = await browser.new_context(
            ignore_https_errors=True,
            no_viewport=True,
            record_video_dir="./allure-results/videos"
        )
        page = await context.new_page()

        # Handle resizing
        await page.evaluate("window.resizeTo(screen.width, screen.height)")
        await page.wait_for_load_state("load")

        # Get configuration
        config_filename = request.config.getoption("--config", default="local-config.yaml")
        config_manager = ConfigurationManager()
        config = config_manager.get_config(config_filename)

        try:
            await handle_console_messages(page)
            yield page, config
        finally:
            # Finalize video recording before closing the page
            video_path = await page.video.path()
            if video_path:
                LOGGER.info(f"Video recorded at: {video_path}")
                allure.attach.file(video_path, name="Test Video", attachment_type=allure.attachment_type.MP4)

            await page.close()
            await context.close()
            await browser.close()
            LOGGER.info("Closed page, context, and browser")
