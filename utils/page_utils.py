
from typing import List

CART_BUTTON_NAME = ["Add to cart", "Remove"]

def select_button(page, locator_name: str, bt_text: str):
    locator_area = page.locator(locator_name)
    filtering_elements = locator_area.locator("*", has_text=f"{bt_text}")
    return filtering_elements.get_by_role("button").all()

# def select_options(page,  option_text: str):
#     return page.locator(f"//span[contains(@class, '{option_text}')]")


def cart_counter(page) -> int:
    # Locate the cart badge element
    badge_element = page.locator('span.shopping_cart_badge[data-test="shopping-cart-badge"]').first

    # Extract the badge count text
    badge_text = badge_element.inner_text()

    # Convert the text to an integer
    badge_count = int(badge_text)

    return badge_count
