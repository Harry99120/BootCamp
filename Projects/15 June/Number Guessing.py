import random

n = random.randint(1, 100)

max_tries = 10
tries = 0

while tries < max_tries:
    try:
        a = int(input("Guess a number between 1 and 100: "))
        tries += 1
        if a < n:
            print("Very Low")
        elif a > n:
            print("Too high!")
        else:
            print("Huraaaaaahhhhhh ! You guessed the number.")
            break
    except ValueError:
        print("Invalid Entry Please enter an integer.")

if tries == max_tries:
    print("Sorry, you have reached the maximum number of tries.")
    print("The number was:", n)
