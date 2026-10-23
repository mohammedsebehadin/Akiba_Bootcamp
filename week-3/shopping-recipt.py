def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        if item["price"] < 0:
            raise ValueError("Price cannot be negative")

        if item["quantity"] < 0:
            raise ValueError("Quantity cannot be negative")

        subtotal += item["price"] * item["quantity"]

        return subtotal


def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05

    return 0.0


def calculate_tax(amount, tax_rate):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")

    return amount * tax_rate


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount, tax_rate)
    total = taxable_amount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
    }


items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5},
    {"name": "Laptop", "price": 1500, "quantity": 2},
]

tax_rate = 0.15

receipt = generate_receipt(items, tax_rate)

print("========== RECEIPT ==========")

for item in items:
    item_total = item["price"] * item["quantity"]
    print(
        f"{item['name']}: {item['quantity']} x "
        f"{item['price']} = {item_total:.2f} Birr"
    )

    print("-----------------------------")
    print(f"Subtotal: {receipt['subtotal']:.2f} Birr")
    print(f"Discount: {receipt['discount']:.2f} Birr")
    print(f"Tax:      {receipt['tax']:.2f} Birr")
    print(f"Total:    {receipt['total']:.2f} Birr")
    print("=============================")