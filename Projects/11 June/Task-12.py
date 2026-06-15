import random
n = random.randint(1,10)
count = 0
while n < 7:
    print(n)
    n = random.randint(1,10)
    count += 1
print(n)
print("Number Generated greater than or equal to 7 is",count) 