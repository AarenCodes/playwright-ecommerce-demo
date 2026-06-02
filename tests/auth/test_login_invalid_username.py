from playwright.sync_api import Page, expect

def test_login_invalid_username(page: Page):

    print("\n[STEP 1] Navigate to login page")

    page.goto("https://www.saucedemo.com")

    print("[PASS] Login page loaded")

    print("\n[STEP 2] Enter invalid credentials")

    page.fill("#user-name", "wrong_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    print("[PASS] Login attempted")

    print("\n[STEP 3] Verify error message")

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )

    print("[PASS] Error message displayed")

    print("\n[STEP 4] Verify user remains on login page")

    expect(page).to_have_url("https://www.saucedemo.com/")

    print("[PASS] User was not logged in")

    print("\n[SUCCESS] Negative login test completed")

def test_login_blank_username(page: Page):

    print("\n[STEP 1] Navigate to login page")

    page.goto("https://www.saucedemo.com")

    print("[PASS] Login page loaded")

    print("\n[STEP 2] Enter username and leave password blank")

    page.fill("#user-name", "")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    print("[PASS] Login attempted")

    print("\n[STEP 3] Verify error message")

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username is required"
    )

    print("[PASS] Error message displayed")

    print("\n[STEP 4] Verify user remains on login page")

    expect(page).to_have_url("https://www.saucedemo.com/")

    print("[PASS] User was not logged in")

    print("\n[SUCCESS] Blank password login test completed")