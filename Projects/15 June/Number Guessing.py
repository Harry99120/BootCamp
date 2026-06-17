import random 
N = int(input("Guess a number from 0 to 11-->"))
X = random.randint(0,11)
if X == N :
    print("Correct Number")
else :
    print("Not Correct")

