def test_google_title(driver):
    """Verify that Google opens correctly"""
    driver.get("https://www.google.com")
    assert "Google" in driver.title