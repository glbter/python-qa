from selenium.webdriver.common.by import By


class Page:
    def __init__(self, driver, url):
        driver.get(url)
        self.driver = driver


class ComputersPage(Page):
    _url = "http://computer-database.gatling.io/computers"
    _apple_url = "http://computer-database.gatling.io/computers?f=apple"

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def section(self):
        return self.driver.find_element(By.CSS_SELECTOR, "body>section")

    def search_box(self):
        return self.driver.find_element(By.ID, "searchbox")

    def submit_btn(self):
        return self.driver.find_element(By.ID, "searchsubmit")

    def element_from_table(self, indx):
        return self.section().find_element(By.CSS_SELECTOR, "table>tbody")\
            .find_elements(By.CSS_SELECTOR, "tr>td>a")[indx]

    def title(self):
        return self.section().find_element(By.CSS_SELECTOR, "h1")
