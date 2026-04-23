# QA Automation Project (Playwright + Pytest)

## 📌 Overview
This project demonstrates UI test automation using:
- Playwright
- Pytest
- Page Object Model (POM)

## 🚀 Features
- Login functionality testing
- Positive & negative scenarios
- Reusable page objects
- Test data separation
- Config-based environment setup
- Allure reporting

## 🧱 Project Structure
- `pages/` → Page Object classes
- `tests/` → Test cases
- `data/` → Test data
- `utils/` → Assertions/helpers
- `conftest.py` → Fixtures

## ⚙️ Setup

```bash
git clone https://github.com/Pallasstyx/qa-automation-playwright.git
cd automated_tests
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install