from modules.menu import MenuItemManager
from modules.cart import CartManager

def menu_management_flow():
    manager = MenuItemManager()
    while True:
        print("\n--- Menu Settings ---")
        print("1. Add New Item")
        print("2. Remove Item")
        print("3. View Menu")
        print("4. Save and Exit to Main")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            try:
                price = float(input("Enter price: "))
                manager.add_item(name, price)
            except ValueError:
                print("Invalid input. Price must be a number.") # 
        elif choice == '2':
            manager.list_items()
            item_id = input("Enter ID to remove: ")
            manager.remove_item(item_id)
        elif choice == '3':
            manager.list_items()
        elif choice == '4':
            manager.save_menu()
            break
        else:
            print("Invalid selection. Please try again.")

"""Write your main logic execution within this function cart_management_flow()"""

def cart_management_flow():
    cart_service = CartManager()
    menu_service = MenuItemManager()
    
    while True:
        print("\n" + "="*40)
        print("          BILLING TERMINAL          ")
        print("="*40)
        
        menu_service.list_items()
        
        print("\n--- Current Order ---")
        current_cart = cart_service.cart
        if not current_cart:
            print("[ EMPTY ]")
        else:
            for item_id, qty in current_cart.items():
                name = menu_service.menu_data.get(item_id, {}).get('name', 'Item')
                print(f"ID {item_id}: {name:<15} x{qty}")
        
        print("-" * 40)
        print("Commands: [ID] [QTY] | 'done' | 'clear'")
        user_input = input("Action >> ").strip().lower()

        if user_input == 'done':
            total = cart_service.calculate_total()
            print(f"\nFinal Bill Total: ${total:.2f}")
            break
            
        if user_input == 'clear':
            cart_service.cart.clear()
            continue

        parts = user_input.split()
        if len(parts) == 2:
            try:
                item_id, qty = parts[0], int(parts[1])
                result = cart_service.update_cart(item_id, qty)
                print(f"[{result['status'].upper()}] {result['message']}")
            except ValueError:
                print("[ERROR] Quantity must be a number.")
        else:
            print("[ERROR] Invalid format. Use: 101 2")

def main():
    while True:
        print("\n===== Coffee Shop System =====")
        print("1. Open Menu (CRUD)")
        print("2. New Bill (Order)")
        print("3. Exit")
        
        choice = input("Select operation: ")
        
        if choice == '1':
            menu_management_flow()
        elif choice == '2':
            cart_management_flow()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input, please use numbers 1-3.")
 

if __name__ == "__main__":
    main()