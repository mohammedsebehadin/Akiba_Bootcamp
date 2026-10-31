expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 1200},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]
print(expenses[0])
def add_expense(expense_list,desc,cat,amt):
    new_expense={
        "description":desc,
        "category":cat,
        "amount":amt

    }
    expense_list.append(new_expense)
    return expense_list

def tot_expense(expense_list):
    tot=0
    for expense in expense_list:
        tot+=expense["amount"]
    return tot
print("initial total:",tot_expense(expenses))
def largest_expense(expense_list):
    largestExpense=0
    largestIndex=0
    for index,expense in enumerate(expense_list):
        if expense['amount']>largestExpense:
            largestExpense=expense['amount']
            largestIndex=index
    return expense_list[largestIndex]
print(largest_expense(expenses))
def filter_expense(expense_list):
    threshold=1000
    for index,expense in enumerate(expense_list):
        if expense['amount']>threshold:
            return expense_list[index]
print("the threshold is amount:1000birr",filter_expense(expenses))    
print("==== analyaztion of expense======")
print(largest_expense(expenses))
print("the threshold is amount:1000birr",filter_expense(expenses))
print(add_expense(expenses,"bus_ticket","transport",8990))






