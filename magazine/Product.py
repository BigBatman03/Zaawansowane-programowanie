"""Products available in the magazine."""

import magazine.utils


class Product:
    """Describe a product and its price."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {magazine.utils.format_price(self.price)}"
