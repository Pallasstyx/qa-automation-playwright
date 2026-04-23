from config import BASE_URL
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
        self.success_message = ".flash.success"


    def navigate(self):
        self.page.goto(f"{BASE_URL}/login")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_login_successful(self):
        return self.page.locator(self.success_message).is_visible()