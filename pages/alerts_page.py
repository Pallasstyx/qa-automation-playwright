from config import BASE_URL


class AlertsPage:
    def __init__(self, page):
        self.page = page
        self.js_alert_button = "button[onclick='jsAlert()']"
        self.js_confirm_button = "button[onclick='jsConfirm()']"
        self.js_prompt_button = "button[onclick='jsPrompt()']"
        self.result_text = "#result"

    def navigate(self):
        self.page.goto(f"{BASE_URL}/javascript_alerts")

    def handle_next_dialog(self, accept=True, prompt_text=None):
        def on_dialog(dialog):
            if prompt_text is not None:
                dialog.accept(prompt_text)
            elif accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.once("dialog", on_dialog)

    def click_js_alert(self):
        self.page.click(self.js_alert_button)

    def click_js_confirm(self):
        self.page.click(self.js_confirm_button)

    def click_js_prompt(self):
        self.page.click(self.js_prompt_button)

    def get_result_text(self):
        return self.page.locator(self.result_text).inner_text()
