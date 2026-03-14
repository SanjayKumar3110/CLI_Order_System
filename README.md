# CLI Coffee Shop Ordering System ☕

A comprehensive Command Line Interface (CLI) application built in Python to manage a coffee shop's menu and process customer orders. The project demonstrates real-world software logic, focusing on user experience, error handling, persistent data storage via JSON, and a clean project structure.

## 🚀 Features

*   **Menu Management (CRUD):** 
    *   Add new items or update prices of existing items.
    *   Remove items from the menu, with dynamic ID re-sequencing.
    *   Menu data is persisted automatically in `data/menu.json`.
*   **Billing Terminal & Interactive Cart:**
    *   Dynamically add items to the cart and specify quantities.
    *   Update quantities or remove items seamlessly.
    *   Review a formatted subtotal and a final invoice before confirming an order.
*   **Graceful Error Handling:**
    *   Input validation protects against negative quantities, non-numeric inputs, and invalid IDs.
    *   Prevents checking out an empty cart.

## 📂 Project Structure

```text
CLI_ORDER_SYSTEM/
│
├── main.py                # Main entry point for the application
├── start.bat              # Batch file to easily launch the app on Windows
├── data/
│   └── menu.json          # Persistent JSON storage for menu items
└── modules/
    ├── cart.py            # CartManager logic (calculating totals, display formatting)
    ├── handler.py         # Main operational flows (Menu settings & Billing loops)
    └── menu.py            # MenuItemManager logic (CRUD operations for the JSON file)
```

## 🛠️ Prerequisites

*   **Python 3.x** installed on your machine.

## 🏃 How to Run

There are two straightforward ways to start the application:

**Option 1: Using the provided bash script (Windows only)**
Simply double-click on `start.bat` in the project folder, or run it through the command prompt:
```bash
start.bat
```

**Option 2: Using Python via Terminal (Cross-platform)**
Navigate to the project root directory and run the main Python script:
```bash
python main.py
```

## 📖 Usage Guide

Upon launching the application, you'll be presented with the Main Menu:

```text
===== Coffee Shop System =====
1. Open Menu (CRUD)
2. New Bill (Order)
3. Exit
```

### 1. Menu Management (`1`)
Select `1` to manage your shop's offerings.
*   **Add New Item (`1`):** You will be prompted for an item name and price. If the name already exists, you'll be asked if you want to update the price.
*   **Remove Item (`2`):** Lists the current items and prompts for the ID you wish to remove.
*   **View Menu (`3`):** Displays the beautifully formatted current menu.
*   **Save and Exit to Main (`4`):** Safely persists your changes and returns to the main loop.

### 2. Billing Terminal (`2`)
Select `2` to process a new customer order.
The terminal will display the current menu and the active order (cart state).

**Commands for the Billing Terminal:**
*   Add/Update item: `[Item ID] [Quantity]` (e.g., `1 2` to add 2 units of Item ID 1)
*   Remove item: `[Item ID]r` (e.g., `1r` to remove Item ID 1 from the cart)
*   Confirm & Checkout: Type `d` (Done) to proceed to the final invoice.
*   Cancel Order: Type `c` to drop the cart and exit.

## 💡 Why I Created This
This project was built to explore how a simple terminal interface can handle the logic a real cafe encounters daily. Instead of just writing scripts, the focus was to build robust user flows—from browsing a dynamic menu without experiencing application-breaking crashes on user typos, to receiving a clean, itemized receipt.
