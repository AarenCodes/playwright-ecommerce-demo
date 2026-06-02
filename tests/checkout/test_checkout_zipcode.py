from playwright.sync_api import Page, expect
from helpers.checkout import go_to_checkout_information_page

def test_checkout_requires_zip_code(page: Page):
    go_to_checkout_information_page(page)

    print("\n[STEP] Leave zip code blank and submit")

    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.click("#continue")

    expect(page.locator('[data-test="error"]')).to_contain_text("Postal Code is required")

    print("[PASS] Zip code validation message displayed")