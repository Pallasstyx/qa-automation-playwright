from config import BASE_URL


class DropdownPage:
    def __init__(self, page):
        self.page = page
        self.dropdown = "#dropdown"

    def navigate(self):
        self.page.goto(f"{BASE_URL}/dropdown")

    def select_option(self, value):
        self.page.select_option(self.dropdown, value)

    def selected_label(self):
        return self.page.locator(f"{self.dropdown} option:checked").inner_text()
