import pytest
from selenium import webdriver
from page import ComputersPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(2)

    pytest.computers_page = ComputersPage(driver, ComputersPage._url)
    pytest.apple_computers_page = ComputersPage(driver, ComputersPage._apple_url)
    try:
        yield driver
    finally:
        driver.quit()
