from config import BASE_URL


class AddRemovePage:
    def __init__(self, page):
        self.page = page
        self.add_button = "button[onclick='addElement()']"
        self.delete_buttons = ".added-manually"

    def navigate(self):
        self.page.goto(f"{BASE_URL}/add_remove_elements/")

    def add_element(self):
        self.page.click(self.add_button)

    def delete_element(self, index=0):
        self.page.locator(self.delete_buttons).nth(index).click()

    def count_elements(self):
        return self.page.locator(self.delete_buttons).count()
