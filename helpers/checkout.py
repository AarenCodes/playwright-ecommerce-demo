from playwright.sync_api import Page, expect
from helpers.login import login

def go_to_checkout_information_page(page: Page):
    login(page)

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    expect(page.locator('[data-test="title"]')).to_have_text("Checkout: Your Information")