from products import Product
from store import Store


def input_menu() -> str:
    """
    Displays the main menu and returns user choice.

    Returns:
        str: The user's menu selection.
    """
    print("\nPlease choose a number:")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")
    return input("Your choice: ")


def show_products(store: Store):
    """
    Prints the list of all active products in the store.

    Args:
        store (Store): The store instance.
    """
    print("\n--- Product List ---")
    for product in store.get_all_products():
        print(product.show())


def show_total_quantity(store: Store):
    """
    Prints the total quantity of all products in the store.

    Args:
        store (Store): The store instance.
    """
    total = store.get_total_quantity()
    print(f"\nTotal quantity in store: {total}")


def handle_order(store: Store):
    """
    Handles user interaction for making an order.

    Args:
        store (Store): The store instance.
    """
    shopping_list = []
    products = store.get_all_products()

    print("\nChoose products to order (type 'done' to finish):")

    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.show()}")

    while True:
        selected = input("Enter product number or 'done': ")

        if selected.lower() == "done":
            break

        if not selected.isdigit() or not (1 <= int(selected) <= len(products)):
            print("Invalid selection. Try again.")
            continue

        product_index = int(selected) - 1
        quantity_str = input("Enter quantity: ")

        if not quantity_str.isdigit():
            print("Quantity must be a positive number.")
            continue

        quantity = int(quantity_str)

        # Check if requested quantity is available
        available_qty = products[product_index].get_quantity()
        if quantity > available_qty:
            print(f"Only {available_qty} units available. Please enter a smaller quantity.")
            continue

        shopping_list.append((products[product_index], quantity))

    if shopping_list:
        try:
            total = store.order(shopping_list)
            print(f"\nTotal order cost: ${total:.2f}")
        except ValueError as error:
            print(f"Order error: {error}")


def start(store: Store):
    """
    Starts the command-line interface for interacting with the store.

    Args:
        store (Store): An instance of the Store class with products.

    Allows the user to:
        - List all active products in the store
        - Show the total quantity of all products
        - Make a multi-product order
        - Quit the application
    """
    print("\n======= Store =======")

    while True:
        choice = input_menu()

        if choice == "1":
            show_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            handle_order(store)
        elif choice == "4":
            print("Thank you for using the store CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# ====== SETUP INITIAL STOCK ======
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = Store(product_list)
    start(best_buy)
