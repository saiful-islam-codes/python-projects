initial_bill = int(input("enter your bill : "))
tip = int(input("Enter '%' of tip : "))

total_bill = initial_bill + (initial_bill * tip /100)

person = int(input("Enter person number : "))

split = total_bill / person

print(f"Total bill is {total_bill}")
print(f"Each person pays {split}")
