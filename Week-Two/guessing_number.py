secret_number = 42

for attempt in range(1, 6):
    guessed_number = int(input("Enter your guess: "))

    if guessed_number == secret_number:
        print("Cherish, you are right!")
        break
    elif attempt < 5:
        print("Incorrect. Try another number.")
    else:
        print("Incorrect. You used all five attempts.")
