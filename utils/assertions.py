def assert_login_success(page):
    assert page.locator(".flash.success").is_visible()

def assert_login_failed(page):
    assert page.locator(".flash.error").is_visible()