inventory = {}

def add_product(name, price, stock):
    key = name.lower()
    if not name or key in inventory or price < 0 or stock < 0:
        raise ValueError("Invalid product details or product already exists")
    inventory[key] = {"name": name, "price": price, "stock": stock}

def update_price(name, price):
    if name.lower() not in inventory or price < 0:
        raise ValueError("Product not found or invalid price")
    inventory[name.lower()]["price"] = price

def increase_stock(name, quantity):
    if name.lower() not in inventory or quantity < 0:
        raise ValueError("Product not found or invalid quantity")
    inventory[name.lower()]["stock"] += quantity

def sell_product(name, quantity):
    product = inventory.get(name.lower())
    if not product or quantity <= 0 or quantity > product["stock"]:
        raise ValueError("Product not found or insufficient stock")
    product["stock"] -= quantity
    return product["price"] * quantity

def total_inventory_value():
    return sum(p["price"] * p["stock"] for p in inventory.values())

def low_stock_report(threshold=5):
    return [p["name"] for p in inventory.values() if p["stock"] < threshold]
if __name__ == "__main__":
                                                                                
        print("--- Adding Products ---")
        add_product("Laptop", 999.99, 10)
        add_product("Mouse", 25.50, 3)     # Low stock item (< 5)
        add_product("Keyboard", 75.00, 15)
        print("Products added successfully!")

print("\n--- Current Inventory Value ---")
print(f"Total Value: ${total_inventory_value():.2f}")

print("\n--- Selling a Product ---")
revenue = sell_product("Laptop", 2)
print(f"Sold 2 Laptops. Revenue generated: ${revenue:.2f}")

print("\n--- Low Stock Report ---")
print(f"Items needing reorder: {low_stock_report()}")

print("\n--- Updated Inventory Value ---")
print(f"Total Value: ${total_inventory_value():.2f}")
