from typing import List, Tuple
from products import Product
from store import Store

def input_menu() -> str:
    print("\nPlease choose a number:")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")
    return input("Your choice: ")

def show_products(store: Store) -> None:
    print("\n--- Product List ---")
    products = store.get_all_products()
    if not products:
        print("No active products available.")
        return
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.show()}")

def show_total_quantity(store: Store) -> None:
    total = store.get_total_quantity()
    print(f"\nTotal quantity in store: {total}")

def get_product_selection(products: List[Product]) -> Tuple[int, int]:
    while True:
        selected = input("Enter product number or 'done': ")
        if selected.lower() == "done":
            raise ValueError("User finished selection")
        if not selected.isdigit():
            print("Please enter a valid number or 'done'.")
            continue
        product_index = int(selected) - 1
        if not (0 <= product_index < len(products)):
            print(f"Please enter a number between 1 and {len(products)}.")
            continue
        quantity = get_quantity_input(products[product_index])
        return product_index, quantity

def get_quantity_input(product: Product) -> int:
    while True:
        quantity_str = input("Enter quantity: ")
        if not quantity_str.isdigit():
            print("Quantity must be a positive number.")
            continue
        quantity = int(quantity_str)
        available_qty = product.get_quantity()
        if quantity <= 0:
            print("Quantity must be positive.")
        elif quantity > available_qty:
            print(f"Only {available_qty} units available. Please enter a smaller quantity.")
        else:
            return quantity

def handle_order(store: Store) -> None:
    shopping_list = []
    products = store.get_all_products()
    if not products:
        print("No active products available for ordering.")
        return
    print("\nChoose products to order (type 'done' to finish):")
    show_products(store)
    try:
        while True:
            product_index, quantity = get_product_selection(products)
            shopping_list.append((products[product_index], quantity))
    except ValueError as e:
        if str(e) != "User finished selection":
            raise
    if not shopping_list:
        print("No items selected. Order cancelled.")
        return
    try:
        total = store.order(shopping_list)
        print(f"\nOrder successful! Total cost: ${total:.2f}")
    except ValueError as error:
        print(f"Order error: {error}")

def main() -> None:
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)

def start(store: Store) -> None:
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
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

