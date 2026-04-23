from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # visible browser
        page = browser.new_page()

        page.goto("https://www.google.com")
        page.fill("textarea[name='q']", "Armine QA automation 😎")
        page.press("textarea[name='q']", "Enter")

        page.wait_for_timeout(3000)

        assert "Armine" in page.title()

        browser.close()