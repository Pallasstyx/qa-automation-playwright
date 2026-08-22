from pages.alerts_page import AlertsPage


def test_accept_js_alert(page):
    alerts = AlertsPage(page)
    alerts.navigate()

    alerts.handle_next_dialog(accept=True)
    alerts.click_js_alert()

    assert alerts.get_result_text() == "You successfully clicked an alert"


def test_dismiss_js_confirm(page):
    alerts = AlertsPage(page)
    alerts.navigate()

    alerts.handle_next_dialog(accept=False)
    alerts.click_js_confirm()

    assert alerts.get_result_text() == "You clicked: Cancel"


def test_accept_js_prompt_with_text(page):
    alerts = AlertsPage(page)
    alerts.navigate()

    alerts.handle_next_dialog(prompt_text="Armine QA")
    alerts.click_js_prompt()

    assert alerts.get_result_text() == "You entered: Armine QA"
