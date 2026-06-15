secret = 42
guess = int(input("Enter your guess: "))
if guess < secret:
    print("Too low")
    print("You are", secret - guess, "below the number")
elif guess > secret:
    print("Too high")
    print("You are", guess - secret, "above the number")
else:
    print("Correct!")