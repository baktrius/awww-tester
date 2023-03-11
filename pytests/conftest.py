from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from typing import Iterator


def get_firefox_driver() -> WebDriver:
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager

    return Firefox(service=FirefoxService(GeckoDriverManager().install()))


@pytest.fixture(scope="session")
def driver() -> Iterator[WebDriver]:
    driver: WebDriver = get_firefox_driver()
    yield driver
    driver.quit()
