class Product:
    """
    Represents a product with name, price, and quantity.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product, must be non-negative.
            quantity (int): The quantity in stock, must be non-negative.

        Raises:
            ValueError: If price or quantity is negative, or name is empty.
        """
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name.strip()
        self.price = price
        self.quantity = quantity
        self.active = True

    def is_active(self) -> bool:
        """Returns whether the product is active (available for purchase)."""
        return self.active

    def get_quantity(self) -> int:
        """Returns the current quantity in stock."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Sets the quantity of the product in stock.

        Args:
            quantity (int): The new quantity, must be non-negative.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity

    def activate(self) -> None:
        """Activates the product, making it available for purchase."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the product, making it unavailable for purchase."""
        self.active = False

    def buy(self, requested_quantity: int) -> float:
        """
        Attempts to buy a quantity of the product.

        Args:
            requested_quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If requested_quantity is negative, more than stock, or product is inactive.
        """
        if requested_quantity <= 0:
            raise ValueError("Purchase amount must be positive")
        if not self.is_active():
            raise ValueError("Product is not available for purchase")
        if requested_quantity > self.quantity:
            raise ValueError(f"Not enough stock to buy {requested_quantity} units")

        self.set_quantity(self.quantity - requested_quantity)
        if self.quantity == 0:
            self.deactivate()
        return self.price * requested_quantity

    def show(self) -> str:
        """Returns a string representation of the product."""
        status = "Active" if self.is_active() else "Inactive"
        return f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}, Status: {status}"
