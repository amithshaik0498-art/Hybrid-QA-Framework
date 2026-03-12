# 🚀 Hybrid QA Automation Framework

A professional-grade test automation framework demonstrating the integration of **API Testing (Backend)** and **UI Testing (Frontend)** using a "Hybrid" approach.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Web Framework:** Flask (Internal System Under Test)
* **Testing Tool:** Pytest
* **API Testing:** Requests
* **UI Testing:** Selenium WebDriver (Chrome)
* **Reporting:** Allure / Pytest-HTML

## 🏗️ Architecture: The "Hybrid" Approach
This framework avoids "UI-only" automation by using the API for state management:
1. **Setup:** Uses API `POST` requests to inject test data directly into the application.
2. **Verification:** Uses Selenium to perform end-to-end UI assertions on the browser.
3. **Teardown:** Uses API `DELETE` requests to clean up data, ensuring a "stable and repeatable" test environment.

## 🚀 How to Run

### 1. Start the Application Server
```bash
python app_server/app.py