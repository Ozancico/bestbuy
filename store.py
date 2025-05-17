from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store that manages multiple products.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes a store with a list of products.

        Args:
            products (List[Product]): Initial list of products in the store.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a new product to the store.

        Args:
            product (Product): The product to be added.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: Sum of quantities across all products.
        """
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Returns all active products currently in the store.

        Returns:
            List[Product]: List of active products.
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order consisting of multiple products and quantities.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains
                - a Product instance
                - an integer quantity to purchase

        Returns:
            float: Total cost of the entire order.

        Raises:
            Exception: If any product in the order cannot fulfill the requested quantity.
        """
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
