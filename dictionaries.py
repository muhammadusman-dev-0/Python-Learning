# Topic: Dictionaries
contacts = {
    "Ali": "03001234567",
    "Ahmed": "03007654321",
    "Sara": "03111234567"
}

print("======= CONTACT BOOK =======")
for name, phone in contacts.items():
    print(name, ":", phone)

contacts["Usman"] = "03221234567"
print("\nAfter adding Usman:", contacts)

search_name = input("\nEnter a name to search: ")
if search_name in contacts:
    print(search_name, "phone number:", contacts[search_name])
else:
    print("Contact not found.")
