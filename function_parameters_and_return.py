# Topic: Function Parameters and Return Values
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("======= TEMPERATURE CONVERTER =======")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose 1 or 2: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", round(celsius_to_fahrenheit(celsius), 2))
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", round(fahrenheit_to_celsius(fahrenheit), 2))
else:
    print("Invalid choice.")
