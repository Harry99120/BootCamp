i = int(input("Enter a sequence of number-->").split(","))
sum_even = 0
for n in i:
    try :
        num = int(n)
        if i % 2 == 0 :
            sum_even += num
    except ValueError :
        print("Invalid input.Please enter only numbers seperated by commas")
        break
else :
    print("The sum of even numbers is",sum_even)