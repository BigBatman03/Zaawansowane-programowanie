"""Orders placed in the magazine."""

import magazine.utils


class Order:
    """Describe an order containing products."""

    def __init__(self, products):
        self.products = list(products)

    @property
    def total(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        return (
            f"Order ({len(self.products)} products): "
            f"{magazine.utils.format_price(self.total)}"
        )
