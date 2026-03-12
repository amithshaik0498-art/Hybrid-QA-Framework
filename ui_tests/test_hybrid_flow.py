import requests
import time
from selenium.webdriver.common.by import By


def test_hybrid_flow_with_cleanup(driver):
    item_id = 777  # A specific ID for this test
    unique_name = f"Disposable-Item-{int(time.time())}"
    base_url = "http://127.0.0.1:5000/api/inventory"

    # 1. SETUP: Create the item via API
    payload = {"id": item_id, "name": unique_name, "price": 99.99}
    requests.post(base_url, json=payload)

    try:
        # 2. TEST: Verify in UI
        driver.get("http://127.0.0.1:5000/inventory-web")
        items = driver.find_elements(By.CLASS_NAME, "inventory-item")
        item_texts = [item.text for item in items]

        assert any(unique_name in text for text in item_texts)
        print(f"Successfully verified {unique_name} in UI.")

    finally:
        # 3. TEARDOWN: Delete the item so the next test starts fresh
        delete_url = f"{base_url}/{item_id}"
        response = requests.delete(delete_url)

        if response.status_code == 200:
            print(f"Cleanup Successful: Item {item_id} removed.")