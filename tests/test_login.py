from playwright.sync_api import Page, expect

def test_login(page: Page):

    print("\n[STEP 1] Navigate to login page")

    page.goto("https://www.saucedemo.com")

    print("[PASS] Login page loaded")

    print("\n[STEP 2] Enter credentials")
    
    # credentials
    print("\n[STEP 2] standard_user / secret_sauce")

    # enter credentials
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    print("[PASS] Credentials entered")

    print("\n[STEP 3] Click login")

    page.click("#login-button")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    print("[PASS] Login successful")

    print("\n[SUCCESS] Login test completed")