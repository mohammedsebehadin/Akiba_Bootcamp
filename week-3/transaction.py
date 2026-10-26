balance = 1000.0
transaction_history = []
withdrawal_limit = 1000
total_withdrawal_today = 0

def check_balance():
    global balance
    return balance

def record_transaction(type, amount, balance_after):
    global transaction_history
    record = {"type": type, "amount": amount, "balance_after": balance_after}
    transaction_history.append(record)

def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("The amount must be positive.")

    balance += amount
    print(f"Successfully deposited ${amount:.2f}. New Balance: ${balance:.2f}")
    record_transaction("deposit", amount, balance)
    return balance

def withdrawal(amount):
    global balance, total_withdrawal_today, withdrawal_limit
    if amount <= 0:
        raise ValueError("The amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    if (total_withdrawal_today + amount) > withdrawal_limit:
        raise ValueError("DAILY LIMIT EXCEEDED.")

    balance -= amount
    total_withdrawal_today += amount
    print(f"Successfully withdrew ${amount:.2f}. New Balance: ${balance:.2f}")
    record_transaction("withdrawal", amount, balance)
    return balance


deposit(500)
withdrawal(200)
