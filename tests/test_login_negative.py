from pages.login_page import LoginPage
from data.test_data import INVALID_USER

def test_invalid_login(page):
    login = LoginPage(page)

    login.navigate()  

    login.login(INVALID_USER["username"], INVALID_USER["password"])

    assert "invalid" in page.locator(".flash.error").inner_text().lower()