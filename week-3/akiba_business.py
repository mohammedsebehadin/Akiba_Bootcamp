
# product management
products=[
    {"name ":"mobile phone","quantity":"4","unit price":"30,000"},
    {"name":"computer","quantity":"7","unit price":"100,000"}
]
def add_product(product_list,name,quantity,unit_price):
    new_product={
        "name":name,
        "quantity":quantity,
        "unit price":unit_price
    }
    product_list.append(new_product)
    return product_list
# print(add_product(product,"table","9","3000"))
def search_product(name):
    for product in products:
        if name