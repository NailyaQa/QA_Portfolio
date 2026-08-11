from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    def get_total_orders_count(self):
        return int(
            self.get_text(
                OrderFeedLocators.TOTAL_ORDERS_COUNT
            )
        )

    def get_today_orders_count(self):
        return int(
            self.get_text(
                OrderFeedLocators.TODAY_ORDERS_COUNT
            )
        )

    def get_orders_in_progress(self):
        return self.find_elements(
            OrderFeedLocators.ORDER_NUMBERS_IN_PROGRESS
        )

    def is_order_in_progress(self, order_number):
        orders = self.get_orders_in_progress()

        return any(
            order.text.strip().isdigit()
            and int(order.text.strip()) == int(order_number)
            for order in orders
        )

    def wait_for_total_orders_count_increase(
        self,
        old_count
    ):
        return self.wait.until(
            lambda driver:
            self.get_total_orders_count() > old_count
        )

    def wait_for_today_orders_count_increase(
        self,
        old_count
    ):
        return self.wait.until(
            lambda driver:
            self.get_today_orders_count() > old_count
        )

    def wait_for_order_in_progress(self, order_number):
        return self.wait.until(
            lambda driver:
            self.is_order_in_progress(order_number)
        )
    