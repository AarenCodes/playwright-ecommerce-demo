from playwright.sync_api import Page, expect
from helpers.checkout import go_to_checkout_information_page


def test_checkout_requires_last_name(page: Page):
    go_to_checkout_information_page(page)

    print("\n[TEST] Leave last name blank and submit")

    page.fill("#first-name", "John")
    page.fill("#postal-code", "12345")
    page.click("#continue")

    expect(page.locator('[data-test="error"]')).to_contain_text("Last Name is required")

    print("[PASS] Last name validation message displayed")