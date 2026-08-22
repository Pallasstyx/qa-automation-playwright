import pytest
from pages.dropdown_page import DropdownPage


@pytest.mark.parametrize("value,label", [("1", "Option 1"), ("2", "Option 2")])
def test_select_dropdown_option(page, value, label):
    dropdown = DropdownPage(page)
    dropdown.navigate()

    dropdown.select_option(value)

    assert dropdown.selected_label() == label
