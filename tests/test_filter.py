from playwright.sync_api import Page, expect
from helpers.login import login

def test_filter(page: Page):
    print("*Test Filter Functionality*")

    print("\n [STEP 1] login to the app")
    login(page)
    print("\n [STEP 1] login successful")

    print("\n [STEP 2] Open filter dropdown")
   
# Get the filter dropdown element, and assert it's visible, enabled, and has the default value of "az"
    print("\n [STEP 3] Assert filter dropdown is visible, enabled, and has default value of 'az'")
    filter_dropdown = page.locator('[data-test="product-sort-container"]')
    print("\n [PASS] Filter dropdown is visible, enabled, and has default value of 'az'")

# Assert the filter dropdown is visible, enabled, and has the default value of "az"
    print("\n [STEP 4] Assert filter dropdown is visible, enabled, and has default value of 'az'")
    expect(filter_dropdown).to_be_visible()
    expect(filter_dropdown).to_be_enabled()
    expect(filter_dropdown).to_have_value("az")
    print("\n [PASS] Filter dropdown is visible, enabled, and has default value of 'az'")

# Sort by name (Z to A)
def test_sort_name_descending(page: Page):
    print("*Test Name Sort Descending Order*")
    print("\n [STEP 1] login to the app")
    login(page)
    print("\n [STEP 1] login successful")

    # Step 2, Sort by name (Z to A)
    print("\n [STEP 2] Sort by name (Z to A)")
    page.select_option('[data-test="product-sort-container"]','za')
    items = page.locator(".inventory_item_name").all_text_contents()
    assert items[0] == "Test.allTheThings() T-Shirt (Red)"
    assert items[-1] == "Sauce Labs Backpack"
    print("\n [PASS] Items are sorted by name in descending order")
    pass

# Sort by price (low to high)
def test_sort_price_low_to_high(page: Page):
    print("*Test Price Sort Low to High*")
    print("\n [STEP 1] login to the app")
    login(page)
    print("\n [STEP 1] login successful")
    print("\n [STEP 2] Sort by price (low to high)")
    page.select_option('[data-test="product-sort-container"]','lohi')

    print("\n [STEP 4] Get the price elements and extract their text content, convert to float, and assert the first item is the cheapest and the last item is the most expensive")
# Get the price elements and extract their text content, convert to float, and assert the first item is the cheapest and the last item is the most expensive
    prices = page.locator(".inventory_item_price").all_text_contents()
    prices = [float(price.replace("$", "")) for price in prices]
    assert prices == sorted(prices)
    print("\n [PASS] Items are sorted by price in ascending order")
    pass

# Sort by price (high to low)
def test_sort_price_high_to_low(page: Page):
    print("*Test Price Sort High to Low*")
    print("\n [STEP 1] login to the app")
    login(page)
    print("\n [STEP 1] login successful")
    print("\n [STEP 2] Sort by price (high to low)")
    page.select_option('[data-test="product-sort-container"]','hilo')
    prices = page.locator(".inventory_item_price").all_text_contents()
    prices = [float(price.replace("$", ""))for price in prices]
    # Reverse sort the prices and assert the first item is the most expensive and the last item is the cheapest
    assert prices == sorted(prices, reverse=True)
    print("\n [PASS] Items are sorted by price in descending order")
    pass
