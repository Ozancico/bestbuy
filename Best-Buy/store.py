from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store holding multiple products and processing orders.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes the store with a list of products.

        Args:
            products (List[Product]): Initial product inventory.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store's inventory.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from inventory if it exists.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in stock.

        Returns:
            int: Sum of quantities of active products.
        """
        return sum(p.get_quantity() for p in self.products if p.is_active())

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products.

        Returns:
            List[Product]: Active products list.
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order consisting of multiple products.

        Args:
            shopping_list (List[Tuple[Product, int]]): List of (product, quantity) tuples.

        Returns:
            float: Total cost of the order.

        Raises:
            ValueError: If purchase quantity exceeds stock.
        """
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
