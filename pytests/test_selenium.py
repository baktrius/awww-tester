from selenium.webdriver.remote.webdriver import WebDriver
from helper import get_url, fd_input


def test_resizing_is_smooth(driver: WebDriver):
    driver.get(get_url())
    driver.set_window_position(0, 0)
    driver.set_window_size(1024, 768)
    fd_input("Resolution 1024x768")
    for i in range(50):
        driver.set_window_size(1024 + 4 * i, 768 + 3 * i)
    driver.set_window_size(1280, 720)
    fd_input("Resolution 1280x720")
    for i in range(30):
        driver.set_window_size(1280 + 16 * i, 720 + 9 * i)
