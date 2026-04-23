from pages.login_page import LoginPage
from data.test_data import VALID_USER

def test_login(page):
    login = LoginPage(page)

    login.navigate()  

    login.login(VALID_USER["username"], VALID_USER["password"])

    assert login.is_login_successful()