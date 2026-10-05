#! python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

BASE_URL = "https://ya.ru/"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    d = webdriver.Chrome(options=options)
    d.implicitly_wait(10)
    yield d
    d.quit()

def test_search_field_exists(driver):
    driver.get(BASE_URL)
    search_input = WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.NAME, "text"))
    )
    assert search_input.is_displayed()

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])