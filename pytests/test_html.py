from subprocess import run
from helper import get_html_paths

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from helper import get_css_absolute_paths, fd_input

def test_html_w3c(driver: WebDriver):
    files = get_html_paths()
    for file in files:
        driver.get("https://validator.w3.org/#validate_by_upload")
        file_input = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.ID, "uploaded_file")
        )

        file_input.send_keys(file)
        file_input.submit()

        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.ID, "results")
        )

        success = driver.find_elements(By.CLASS_NAME, "success")

        if len(success) == 0:
            fd_input("Press enter to continue...")
            pytest.fail(f"W3C html validation failed for {file}.")

def test_html_is_valid():
    cmd = f"npx html-validate {' '.join(get_html_paths())}"
    assert run(cmd, shell=True).returncode == 0
