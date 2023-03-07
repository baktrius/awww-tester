from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from typing import Iterator


def get_firefox_driver() -> WebDriver:
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager

    return Firefox(service=FirefoxService(GeckoDriverManager().install()))


@pytest.fixture
def driver() -> Iterator[WebDriver]:
    driver: WebDriver = get_firefox_driver()
    yield driver
    driver.quit()


def test_eight_components(driver: WebDriver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    driver.set_window_position(0, 0)
    driver.set_window_size(1024, 768)
    driver.save_screenshot("test.png")
    for i in range(50):
        driver.set_window_size(1024 + 4 * i, 768 + 3 * i)
    driver.set_window_size(1280, 720)
    driver.save_screenshot("test2.png")
    for i in range(30):
        driver.set_window_size(1280 + 16 * i, 720 + 9 * i)
    assert value == "Received!"
