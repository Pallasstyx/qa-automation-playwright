from pages.add_remove_page import AddRemovePage


def test_add_multiple_elements(page):
    add_remove = AddRemovePage(page)
    add_remove.navigate()

    for _ in range(3):
        add_remove.add_element()

    assert add_remove.count_elements() == 3


def test_delete_element(page):
    add_remove = AddRemovePage(page)
    add_remove.navigate()

    add_remove.add_element()
    add_remove.delete_element()

    assert add_remove.count_elements() == 0
