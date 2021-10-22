import re
import allure
import pytest


@allure.suite('search by key word')
@allure.story('testing ui, doing labs')
def test_search(driver):
    driver.get("http://computer-database.gatling.io/computers")

    with allure.step('find by key word'):
        pytest.computers_page.search_box().send_keys("apple")
        pytest.computers_page.submit_btn().click()

    with allure.step('check page'):
        title = pytest.computers_page.title().text
        assert title == "13 computers found"


@allure.suite('click on element')
@allure.story('testing ui, doing labs')
@pytest.mark.parametrize("indx", [i for i in range(1, 10)])
def test_click_computer(driver, indx):
    driver.get("http://computer-database.gatling.io/computers?f=apple")

    with allure.step('test click on reference'):
        pytest.apple_computers_page.element_from_table(indx).click()

        url = driver.current_url
        assert re.match(r'http://computer-database.gatling.io/computers/\d+', url)
