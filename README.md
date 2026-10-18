# UI Automation Tests (Playwright + Pytest)

UI test automation in Python using Playwright, Pytest and the Page Object Model.

Tests run against [The Internet](https://the-internet.herokuapp.com), a practice site with common UI patterns: login forms, JavaScript alerts, checkboxes, dropdowns and dynamically loaded content.

## What is tested

| Area | Test file | Scenarios |
| --- | --- | --- |
| Login | `test_login.py`, `test_login_negative.py` | Valid login succeeds; invalid credentials show an error message |
| JavaScript alerts | `test_alerts.py` | Accept an alert, dismiss a confirm, type into a prompt |
| Checkboxes | `test_checkboxes.py` | Default state of each checkbox and toggling it |
| Dropdown | `test_dropdown.py` | Selecting each option (parametrized) |
| Dynamic loading | `test_dynamic_loading.py` | Waiting for hidden and late-rendered elements (2 variants, parametrized) |
| Add/remove elements | `test_add_remove_elements.py` | Adding several elements and deleting one |

## How it is built

- **Page Object Model**: each page has its own class in `pages/` with its locators and actions, so tests read like user steps and locator changes are fixed in one place.
- **Fixtures**: `conftest.py` provides a session-scoped `browser` fixture, so Chromium launches once per run, and a function-scoped `page` fixture that gives each test a fresh browser context — test isolation without relaunching the browser for every test.
- **Test data separation**: credentials live in `data/test_data.py`, not inside the tests.
- **Config**: the base URL lives in `config.py`.
- **Parametrization**: `@pytest.mark.parametrize` runs the same test with different inputs.
- **Reporting**: Allure results through `allure-pytest`.

## Project structure

```
qa-automation-playwright/
├── pages/            # Page Object classes
├── tests/            # Test cases
├── data/             # Test data
├── conftest.py       # Pytest fixtures
├── config.py         # Base URL
├── pytest.ini
└── requirements.txt
```

## Setup and run

Requires Python 3.12.

```bash
git clone https://github.com/Pallasstyx/qa-automation-playwright.git
cd qa-automation-playwright
python3.12 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install

pytest                          # run all tests
pytest tests/test_login.py      # run one file
```

### Allure report

```bash
pytest --alluredir=allure-results
allure serve allure-results     # needs the Allure CLI installed
```

## Tech stack

Python · Playwright · Pytest · Allure
