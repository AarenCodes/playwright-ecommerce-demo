from playwright.sync_api import Page, expect

def test_add_to_cart(page: Page):

    print("\n[STEP 1] Navigate to login page")

    page.goto("https://www.saucedemo.com")

    print("[PASS] Login page loaded")

    print("\n[STEP 2] Login")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    print("[PASS] Login successful")

    print("\n[STEP 3] Add backpack to cart")

    page.click("#add-to-cart-sauce-labs-backpack")

    print("[PASS] Backpack added")

    print("\n[STEP 4] Verify cart badge")

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    print("[PASS] Cart badge shows 1")

    print("\n[SUCCESS] Add-to-cart test completed")