from config import BASE_URL


class DynamicLoadingPage:
    def __init__(self, page):
        self.page = page
        self.start_button = "#start button"
        self.finish_text = "#finish h4"

    def navigate(self, example=1):
        self.page.goto(f"{BASE_URL}/dynamic_loading/{example}")

    def start(self):
        self.page.click(self.start_button)

    def wait_for_finish_text(self):
        self.page.wait_for_selector(self.finish_text, state="visible")
        return self.page.locator(self.finish_text).inner_text()
