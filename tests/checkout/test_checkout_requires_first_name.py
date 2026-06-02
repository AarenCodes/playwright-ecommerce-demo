from playwright.sync_api import Page, expect
from helpers.checkout import go_to_checkout_information_page

def test_checkout_requires_first_name(page: Page):
    go_to_checkout_information_page(page)

    print("\n[STEP] Leave first name blank and submit")

    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")
    page.click("#continue")

    expect(page.locator('[data-test="error"]')).to_contain_text("First Name is required")

    print("[PASS] First name validation message displayed")