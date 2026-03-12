import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    # Setup: Initialize Chrome
    options = Options()
    # options.add_argument("--headless") # Add this later for Jenkins/Docker
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver  # This is where the test "lives"

    # Teardown: Close the browser
    driver.quit()