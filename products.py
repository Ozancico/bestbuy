class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True if quantity > 0 else False

    def get_quantity(self) -> int:
        return self.quantity

    def is_active(self) -> bool:
        return self.active

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self.quantity:
            raise Exception(f"Not enough quantity of {self.name}. Available: {self.quantity}")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.price * quantity
