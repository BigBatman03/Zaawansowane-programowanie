"""Application entry point for the magazine example."""

from magazine import Product


def main():
    product = Product.Product("Notebook", 12.5)
    print(product)


if __name__ == "__main__":
    main()
