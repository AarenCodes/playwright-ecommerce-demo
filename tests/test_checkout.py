from playwright.sync_api import Page, expect

def test_checkout_flow(page: Page):
    page.goto("https://www.saucedemo.com")

    #log in to the app
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_timeout(2000)  # 2 seconds

    #add backpack to cart
    page.click("#add-to-cart-sauce-labs-backpack")
    page.wait_for_timeout(2000)

    #navigate to cart
    page.click(".shopping_cart_link")
    page.wait_for_timeout(2000)
    
    #verify on cart page
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    #click checkout
    page.click("#checkout") 

    #fill in checkout info
    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")

    #click continue
    page.click("#continue")
    page.wait_for_timeout(3000)

    # verify on overview page
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Checkout: Overview")

    # click finish
    page.click("#finish")

    # verify on complete page
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")