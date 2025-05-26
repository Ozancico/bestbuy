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

        Raises:
            TypeError: If any item in products is not a Product instance.
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError("All items must be instances of Product class")
        self.products = products.copy()  # Create a copy to avoid external modifications

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the store's inventory if it doesn't already exist.

        Args:
            product (Product): The product to add.

        Raises:
            ValueError: If product with same name already exists.
        """
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product class")

        # Check for duplicate by name
        if any(p.name.lower() == product.name.lower() for p in self.products):
            raise ValueError(f"Product '{product.name}' already exists in inventory")

        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Removes a product from inventory if it exists.

        Args:
            product (Product): The product to remove.

        Raises:
            ValueError: If product is not found in inventory.
        """
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product class")

        # Find product by name (case-insensitive)
        for i, p in enumerate(self.products):
            if p.name.lower() == product.name.lower():
                self.products.pop(i)
                return

        raise ValueError(f"Product '{product.name}' not found in inventory")

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all active products in stock.

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
            ValueError: If purchase quantity exceeds stock or product is inactive.
            TypeError: If any item in shopping_list is not a (Product, int) tuple.
        """
        total = 0.0

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Each shopping list item must be a (Product, int) tuple")
            if not isinstance(item[0], Product) or not isinstance(item[1], int):
                raise TypeError("Each tuple must contain (Product, int)")

            product, quantity = item
            total += product.buy(quantity)

        return total
