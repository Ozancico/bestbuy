from products import Product
from store import Store


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
        print("\nPlease choose a number:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Your choice: ")

        if choice == "1":
            print("\n--- Product List ---")
            for product in store.get_all_products():
                print(product.show())

        if choice == "2":
            print("\nTotal quantity in store:", store.get_total_quantity())

        if choice == "3":
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
                quantity = input("Enter quantity: ")

                if not quantity.isdigit():
                    print("Quantity must be a number.")
                    continue

                shopping_list.append((products[product_index], int(quantity)))

            if shopping_list:
                try:
                    total = store.order(shopping_list)
                    print(f"\nTotal order cost: ${total:.2f}")
                except Exception as e:
                    print(f"Error during order: {e}")

        if choice == "4":
            print("Thank you for using the store CLI. Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please try again.")


# ====== SETUP INITIAL STOCK ======
if __name__ == "__main__":
    """
    Initializes the default store inventory and starts the store interface.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = Store(product_list)
    start(best_buy)
