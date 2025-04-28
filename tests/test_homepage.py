from browser_cfg.browser import PlaywrightPage
from utils.page_utils import *
from playwright.sync_api import expect

class TestSomething(PlaywrightPage):
    

    def test_button_add_to_cart_text_displayed(self, page):

        select_add_button = select_button(
            page=page, locator_name="inventory_container", bt_text=CART_BUTTON_NAME[0]
        )
        for button in select_add_button:
            assert button.text_content() == CART_BUTTON_NAME[0]

    def test_button_remove_text_displayed(self, page):

        select_add_button = select_button(
            page=page, locator_name="inventory_container", bt_text=CART_BUTTON_NAME[1]
        )
        for button in select_add_button:
            assert button.text_content() == CART_BUTTON_NAME[1]

    def test_add_item_to_cart(self, page):
        select_add_button = select_button(
            page=page, locator_name="inventory_container", bt_text=CART_BUTTON_NAME[0]
        )

        for button in select_add_button:
            print(select_add_button)
            print()
            expect(button.text_content()).to_contain_text(CART_BUTTON_NAME[0])
        


    def test_remove_item_from_cart(self, page):
        select_add_button = select_button(
            page=page, locator_name="inventory_container", bt_text=CART_BUTTON_NAME
        )
        for button in select_add_button:
            for dbl_click in range(0, 1):
                button.click()
                assert button.text_content() == CART_BUTTON_NAME[dbl_click]

    def test_cart_item_counter(self, page):
        select_add_button = select_button(
            page=page, locator_name="inventory_container", bt_text=CART_BUTTON_NAME[0]
        )
        num = 0
        for button in select_add_button:
            button.click()
            badge_element = int(
                str(
                    page.locator(
                        'span.shopping_cart_badge[data-test="shopping-cart-badge"]'
                    ).inner_text()
                )
            )
            num += 1
            assert badge_element == num

    def test_decreasing_cart_counter(self, page):
        bt_count = 0
        cart_count = 0
        select_add_button = select_button(
            page=page, locator_name="inventory_container", bt_text=CART_BUTTON_NAME[0]
        )
        for button in select_add_button:
            button.click()
            bt_count += 1
            cart_count = int(
                str(
                    page.locator(
                        'span.shopping_cart_badge[data-test="shopping-cart-badge"]'
                    ).inner_text()
                )
            )

        assert bt_count == cart_count

        select_remove_button = select_button(
            page=page, locator_name="inventory_container", bt_text=CART_BUTTON_NAME[1]
        )
        for rm in select_remove_button:
            rm.click()
            bt_count -= 1
            cart_count -= 1
        assert bt_count == cart_count

    def test_homepage_burger_menu_button(self, page):
        home_burger_menu=select_button(page=page, locator_name="menu_button_container",bt_text="Open Menu")
        for burger_menu in home_burger_menu:
            burger_menu.click()

    def test_product_sort_container_presented(self, page):
        page.locator(f"//select[contains(@class, 'product_sort_container')]").click()
