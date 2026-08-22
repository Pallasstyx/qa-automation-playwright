import pytest
from pages.dynamic_loading_page import DynamicLoadingPage


@pytest.mark.parametrize("example", [1, 2])
def test_element_appears_after_loading(page, example):
    dynamic_loading = DynamicLoadingPage(page)
    dynamic_loading.navigate(example)

    dynamic_loading.start()

    assert dynamic_loading.wait_for_finish_text() == "Hello World!"
