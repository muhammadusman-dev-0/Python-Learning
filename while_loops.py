# Topic: While Loops
secret_number = 7
guess = None
attempts = 0

print("======= NUMBER GUESSING GAME =======")
while guess != secret_number:
    guess = int(input("Guess a number from 1 to 10: "))
    attempts += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Correct! Attempts:", attempts)
