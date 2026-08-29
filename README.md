# Web & API Test Automation Suite

A test automation project demonstrating UI automation (Selenium WebDriver) and API testing (Python `requests`), built with `pytest`.

## What this project covers

**UI Automation (Selenium)**
- Login flow validation (valid/invalid credentials)
- Product search functionality
- Add-to-cart flow
- Form field validation

**API Testing**
- GET / POST / PUT / DELETE requests against a REST API
- Status code and response schema validation
- Negative test cases (invalid input, missing fields)

## Tech Stack
- Python 3
- Selenium WebDriver
- pytest (test runner + assertions)
- requests (API testing)
- Chrome + ChromeDriver

## Project Structure
```
qa-automation-suite/
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_cart.py
├── api_tests/
│   └── test_api_users.py
├── requirements.txt
└── README.md
```

## How to run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run UI tests:
   ```
   pytest tests/ -v
   ```

3. Run API tests:
   ```
   pytest api_tests/ -v
   ```

4. Run everything with an HTML report:
   ```
   pytest --html=report.html
   ```

## Test Sites Used
- UI tests target [the-internet.herokuapp.com](https://the-internet.herokuapp.com) — a public site built specifically for automation practice.
- API tests target [reqres.in](https://reqres.in) — a free public REST API for testing purposes.

## Sample Test Case (Login)

| Field | Detail |
|---|---|
| Test ID | TC_LOGIN_01 |
| Objective | Verify login fails with invalid credentials |
| Steps | 1. Navigate to login page 2. Enter invalid username/password 3. Click submit |
| Expected Result | Error message displayed, user not redirected |
| Actual Result | (fill in after running) |
| Status | Pass/Fail |

## Notes
This project was built to practice test automation fundamentals: writing maintainable Selenium locators, structuring pytest test suites, and validating REST APIs — as part of preparing for QA Automation roles.
