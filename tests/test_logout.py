from playwright.sync_api import Page, expect

def test_logout(page: Page):

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

    print("\n[STEP 4] Open hamburger menu to click logout")
    page.click("#react-burger-menu-btn")

    print("\n[STEP 5] Validate Hamburger menu opened logout")
    expect(page.locator(".bm-menu-wrap")).to_be_visible()

    print("[PASS] Hamburger menu opened")

    print("\n[STEP 6] Click logout")
    page.click("#logout_sidebar_link")

    print("\n[STEP 7] Validate logout successful")
    expect(page).to_have_url("https://www.saucedemo.com/")

    print("\n[SUCCESS] Logout test completed")