a = int(input("Enter a number--> "))
b = int(input("Enter a number--> "))
c = int(input("Enter a number--> "))
if a > b :
    if a > c :
        print("a is largest")
else :
    if b > c :
        if b > a :
            print("b is largest")
    else :
        print("c is largest")