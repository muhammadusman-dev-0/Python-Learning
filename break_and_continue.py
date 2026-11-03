# Topic: break and continue
print("======= NUMBER FILTERING =======")

for number in range(1, 16):
    if number == 12:
        print("Stopping at 12.")
        break

    if number % 2 == 0:
        continue

    print("Odd number:", number)
