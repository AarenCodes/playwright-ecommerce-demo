from playwright.sync_api import Page, expect
from helpers.checkout import go_to_checkout_information_page

def test_checkout_flow(page: Page):

    print("\n[STEP 1] Navigate to checkout information page")

    go_to_checkout_information_page(page)

    print("[PASS] Checkout information page loaded")

    print("\n[STEP 2] Enter customer information")

    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")

    print("[PASS] Customer information entered")

    print("\n[STEP 3] Continue to checkout overview")

    page.click("#continue")

    expect(page.locator('[data-test="title"]')).to_have_text(
        "Checkout: Overview"
    )

    print("[PASS] Checkout overview page loaded")

    print("\n[STEP 4] Finish order")

    page.click("#finish")

    print("[PASS] Finish button clicked")

    print("\n[STEP 5] Verify order completion")

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )

    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )

    print("[PASS] Order completed successfully")

    print("\n[SUCCESS] Checkout flow test completed")