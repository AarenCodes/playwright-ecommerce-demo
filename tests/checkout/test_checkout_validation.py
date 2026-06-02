from playwright.sync_api import Page, expect
from helpers.checkout import go_to_checkout_information_page

def go_to_checkout_information_page(page: Page):
    print("\n[HELPER] Navigate to checkout information page")

    go_to_checkout_information_page(page)

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    expect(page.locator('[data-test="title"]')).to_have_text("Checkout: Your Information")

    print("[PASS] Checkout information page loaded")
