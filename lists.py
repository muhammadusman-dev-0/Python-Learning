# Topic: Lists
shopping_list = ["Milk", "Bread", "Eggs"]

print("Current shopping list:", shopping_list)
shopping_list.append("Rice")
print("After adding Rice:", shopping_list)

shopping_list.remove("Bread")
print("After removing Bread:", shopping_list)

print("\nYour items:")
for item in shopping_list:
    print("-", item)

print("Total items:", len(shopping_list))
