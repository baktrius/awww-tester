from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from helper import get_url
import time


def test_resizing_is_smooth(driver: WebDriver):
    driver.get(get_url())
    driver.set_window_position(0, 0)
    driver.set_window_size(1024, 768)
    time.sleep(2)
    for i in range(50):
        start = time.time()
        driver.set_window_size(1024 + 4 * i, 768 + 3 * i)
        time.sleep(max(0, start + 0.07 - time.time()))
    driver.set_window_size(1280, 720)
    time.sleep(2)
    for i in range(60):
        start = time.time()
        driver.set_window_size(1280 + 8 * i, 720 + int(4.5 * i))
        time.sleep(max(0, start + 0.07 - time.time()))


def test_dark_mode(driver: WebDriver):
    driver.get(get_url())
    # trying to automatically change mode
    els = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for el in els:
        if el.is_displayed():
            el.click()
            time.sleep(1)
    els = driver.find_elements(By.CSS_SELECTOR, "label")
    for el in els:
        if el.is_displayed():
            el.click()
            time.sleep(1)
    driver.execute_script("""
    document.documentElement.classList.add('mode2')
    document.documentElement.classList.add('darkmode')
    document.documentElement.classList.remove('lightmode')""")
    time.sleep(1)


def test_small_resolution(driver: WebDriver):
    driver.get(get_url())
    driver.set_window_size(400, 600)
    time.sleep(2)
    driver.set_window_size(500, 700)
    time.sleep(2)
    driver.set_window_size(800, 1000)
    time.sleep(2)
    driver.set_window_size(1000, 800)
    time.sleep(2)
