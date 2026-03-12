import requests
import pytest

# This is our base URL (just like your Postman variable)
BASE_URL = "http://127.0.0.1:5000/api/inventory"


def test_get_inventory_status_code():
    """Verify that the GET request returns a 200 OK status"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_get_inventory_data_content():
    """Verify the API returns the correct initial data"""
    response = requests.get(BASE_URL)
    data = response.json()

    # Check if we got a list and it's not empty
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["name"] == "Standard Backpack"


def test_add_new_item_to_inventory():
    """Verify that we can add a new item via POST"""
    new_item = {
        "id": 5,
        "name": "Automation Pro Hoodie",
        "price": 55.00
    }

    # Send the POST request
    response = requests.post(BASE_URL, json=new_item)

    # Assertions
    assert response.status_code == 201
    assert response.json()["name"] == "Automation Pro Hoodie"