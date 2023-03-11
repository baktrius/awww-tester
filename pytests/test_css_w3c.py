################################################################################
################################################################################
##                                                                             #
##  Module containing tests checking correctness of CSS code, utilizing vali-  #
##  dation service provided by W3C at https://jigsaw.w3.org/css-validator/ .   #
##                                                                             #
##  Notably, provided tests depend on get_css_paths() function                 #
##  from the utils module.                                                     #
##                                                                             #
##  Asserts failing mean that something unexpected has happened (perhaps       #
##  something on the page changed) and are to be treated as tests errors       #
##  (as opposed to test fails), inspected and fixed.                           #
##                                                                             #
################################################################################
                                                                               #
__author__ = "Wojciech Drozd"                                                  #
__contact__ = "wojciech.drozd@mimuw.students.edu.pl"                           #
__copyright__ = "UW 2023"                                                      #
__credits__ = ["Krzysztof Rogowski"]                                           #
__status__ = "Development"                                                     #
                                                                               #
################################################################################

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from typing import Iterator
from helper import get_css_paths

# TODO: this next section is copied from test_selenium.py
# it is to be organized in a better way by someone who knows python well

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

"""
    Function used to wait for a page (for example one that was navigated to)
    to get (at least somewhat) loaded/ready.

    Meant to be passed to WebDriverWait(driver, timeout).until(<here>).

    Inspiration:
    https://www.selenium.dev/documentation/webdriver/waits/#explicit-wait
"""
def document_initialised(driver):
    return driver.execute_script("return document.readyState == 'complete'")

#   TODO: use docblocks properly.

"""
    Tests correctness of .css files.

    Searches for "congrats" element in result presentation.
    Ignores warnings - at least those which don't stop W3C from granting
    the validated file/page a badge.

    :parameter driver - selenium driver
"""
def test_css_w3c(driver: WebDriver):
    # TODO: lots of code shared with test_css_w3c_strict - deduplicate!
    files_to_check = get_css_paths();
    for file in files_to_check:
        driver.get("https://jigsaw.w3.org/css-validator/#validate_by_upload")

        # This is an explicit wait.
        # Important: don't mix implicit and explicit waits
        #   in one driver session.
        file_input = WebDriverWait(driver, timeout=10)  \
                        .until(lambda d: d.find_element(by=By.ID, value="file"))

        file_input.send_keys(file)
        file_input.submit()

        ### File submitted, waiting for the results. ###

        WebDriverWait(driver, timeout=10).until(document_initialised)

        # Note: this will throw if results_container doesn't appear
        WebDriverWait(driver, timeout=10)   \
            .until(lambda d: d.find_element(by=By.ID, value="results_container"))

        # Note: find_elements() is used, so that no exception is thrown
        # in case no such element exists.
        # Would catching the exception be a better aproach? TODO
        congrats_elements = driver.find_elements(by=By.ID, value="congrats")
        assert len(congrats_elements) <= 1 # sanity check
        if len(congrats_elements) == 0:
            # TODO: possible improvement - how many errors, first error.
            pytest.fail(f"W3C doesn't approve file {file}")

        # Debug: WebDriverWait(driver, timeout=10).until(never)

"""
    Helper function to extract inforation about a warning.

    Takes in a selenium's WebElement representing a table row
    with information about a warning (as it was displayed by W3C).

    Returns a triple containing:
        0: (int) level of warning
        1: (string) warning message/explanation
        2: (int) number of the line of code that triggered the warning
"""
def w3c_warning_destructure(warning_tr):
    warning_tds = warning_tr.find_elements(by=By.TAG_NAME, value="td")
    # Exactly three elements are expected: the 1st with line number,
    # 2nd - with code context (often empty, we omit it here),
    # 3rd - with warning level and message/explanation.
    assert len(warning_tds) == 3
    assert warning_tds[0].get_attribute("class") == "linenumber"
    assert warning_tds[2].get_attribute("class").startswith("level")

    # Here 5 means len("level") - to get class without "level" prefix.
    w_level = int(warning_tds[2].get_attribute("class")[5]);
    w_explanation = warning_tds[2].text
    w_linenumber = int(warning_tds[0].text)
    return (w_level, w_explanation, w_linenumber)

"""
    Tests correctness of .css files.

    Treats warnings of level equal or greater than :parameter threshold
    as errors. By default (and when testing) ignores warnings of level 0
    and below (threshold is set to 1).

    For some context, here are some common "mistakes" triggering
    level 0 warnings:
        - using variables
        - using vendor-specific extensions

    :parameter driver - selenium driver
    :parameter threshold - minimal warning level treated as an error (default 1)
"""
# Potential TODO: disable/ignore unimportant warnings by changing settings?
# TODO: lots of shared code - deduplicate!
def test_css_w3c_strict(driver: WebDriver, threshold=1):
    files_to_check = get_css_paths();
    for file in files_to_check:
        driver.get("https://jigsaw.w3.org/css-validator/#validate_by_upload")

        # This is an explicit wait.
        # Important: don't mix implicit and explicit waits
        #   in one driver session.
        file_input = WebDriverWait(driver, timeout=10)  \
                        .until(lambda d: d.find_element(by=By.ID, value="file"))

        file_input.send_keys(file)
        file_input.submit()

        ### File submitted, waiting for the results. ###

        WebDriverWait(driver, timeout=10).until(document_initialised)

        # Note: this will throw if results_container doesn't appear
        WebDriverWait(driver, timeout=10)   \
            .until(lambda d: d.find_element(by=By.ID, value="results_container"))

        # Note: find_elements() is used, so that no exception is thrown
        # in case no such element exists.
        # Would catching the exception be better? TODO
        congrats_elements = driver.find_elements(by=By.ID, value="congrats")
        assert len(congrats_elements) <= 1 # sanity check
        if len(congrats_elements) == 0:
            # TODO: possible improvement - how many errors, first error.
            pytest.fail(f"W3C doesn't approve file {file}")

        # TODO TODO TODO: deduplicate code above by using repeated code
        # OR putting below code in a callback parameter
        # OR disabling not important warnings by selecting appropriate option.

        warning_elements = driver.find_elements(
                                by=By.CSS_SELECTOR,
                                value="div.warning-section tr.warning"
                            )

        ### Collecting some information about warnings ###
        # Notably one example warning of the highest level present.
        highest_level = -1
        one_highest_explanation = ''
        eplanation_for_lineno = -1 # line number where example warning occured
        highest_level_count = 0
        above_threshold_count = 0
        # total_count = len(warning_elements)

        for warning_tr in warning_elements:
            level, explanation, lineno = w3c_warning_destructure(warning_tr)
            if level > highest_level:
                highest_level = level
                highest_level_count = 1
                one_highest_explanation = explanation
                explanation_for_lineno = lineno
            elif level == highest_level:
                highest_level_count += 1

            if level >= threshold:
                above_threshold_count += 1

        if highest_level >= threshold:
            # TODO: is there a better place to print detailed messages in pytest?
            # Here \x0a stands for \n, because \n doesn't work.
            pytest.fail(
                f"for file {file}\x0aW3C gives {above_threshold_count} "    \
                f"warnings of level >= {threshold}, {highest_level_count} " \
                f"of them being level {highest_level}.\x0a"                 \
                f"For instance, a warning of this level was given at line " \
                f"{lineno}: `{one_highest_explanation}`"
            )

