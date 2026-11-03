# Topic: Functions and return values
def calculate_total(price, quantity):
    return price * quantity

print("======= SIMPLE BILLING CALCULATOR =======")
item_name = input("Enter item name: ")
price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)

print("\nItem:", item_name)
print("Price per item: Rs.", round(price, 2))
print("Quantity:", quantity)
print("Total bill: Rs.", round(total, 2))
