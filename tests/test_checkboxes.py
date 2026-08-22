from pages.checkboxes_page import CheckboxesPage


def test_first_checkbox_starts_unchecked_and_toggles(page):
    checkboxes = CheckboxesPage(page)
    checkboxes.navigate()

    assert checkboxes.is_checked(0) is False
    checkboxes.toggle_checkbox(0)
    assert checkboxes.is_checked(0) is True


def test_second_checkbox_starts_checked_and_toggles(page):
    checkboxes = CheckboxesPage(page)
    checkboxes.navigate()

    assert checkboxes.is_checked(1) is True
    checkboxes.toggle_checkbox(1)
    assert checkboxes.is_checked(1) is False
