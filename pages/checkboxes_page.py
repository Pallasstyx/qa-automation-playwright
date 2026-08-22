from config import BASE_URL


class CheckboxesPage:
    def __init__(self, page):
        self.page = page
        self.checkboxes = "input[type='checkbox']"

    def navigate(self):
        self.page.goto(f"{BASE_URL}/checkboxes")

    def get_checkbox(self, index):
        return self.page.locator(self.checkboxes).nth(index)

    def toggle_checkbox(self, index):
        self.get_checkbox(index).click()

    def is_checked(self, index):
        return self.get_checkbox(index).is_checked()
