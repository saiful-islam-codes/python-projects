# E-Commerce Inventory & Cart System

shop = {
    "id" :{
        "name" : "Laptop",
        "price" : 2300,
    }
}
stock = 5
total = 0
while (stock > 0):
    print(f"{shop['id']['name']} added! price: {shop['id']['price']} taka")
    total = total + shop['id']['price']
    print(f"your total bill {total}.")
    stock = stock - 1
    print(f"stock remaining {stock}")