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
            ValueError: If price or quantity is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def is_active(self) -> bool:
        """Returns whether the product is active (in stock)."""
        return self.active and self.quantity > 0

    def get_quantity(self) -> int:
        """Returns the current quantity in stock."""
        return self.quantity

    def buy(self, amount: int) -> float:
        """
        Attempts to buy a quantity of the product.

        Args:
            amount (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If amount is negative or more than stock.
        """
        if amount <= 0:
            raise ValueError("Purchase amount must be positive")
        if amount > self.quantity:
            raise ValueError(f"Not enough stock to buy {amount} units")

        self.quantity -= amount
        if self.quantity == 0:
            self.active = False
        return self.price * amount

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
