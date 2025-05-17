class Product:
    """
    Represents a product in the store with its name, price, quantity, and availability status.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new product.

        Args:
            name (str): Name of the product.
            price (float): Price of a single unit.
            quantity (int): Available quantity in stock.

        Raises:
            Exception: If name is empty, or price/quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid product data.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity in stock.

        Returns:
            int: Quantity available.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets a new quantity. If quantity is 0, product is deactivated.

        Args:
            quantity (int): New quantity to set.
        """
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active (available for purchase).

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product for sale.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product (not available for sale).
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a human-readable description of the product.

        Returns:
            str: Product information in string format.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Attempts to buy a specific quantity of this product.

        Args:
            quantity (int): Quantity to purchase.

        Returns:
            float: Total price for the purchase.

        Raises:
            Exception: If not enough quantity is available or product is inactive.
        """
        if not self.active:
            raise Exception("Product is not active.")

        if quantity > self.quantity:
            raise Exception("Not enough stock available.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity
