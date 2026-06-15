Year = int(input("Enter Your Year"))

if (Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0):
    print("The Year Is Leap Year")
else :
    print("The Year Is Not a Leap Year")