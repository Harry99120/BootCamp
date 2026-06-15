PIN = int(input("Enter Your Pin-->"))

if PIN == 1234:
    amount = int(input("Enter Your Amount To Be Withdrawn-->"))

    if amount <=5000 :
        print("Dispensed Successfully")
    else :
        print("Limit Exceeds")
    
else :
    print("Invalid PIN Entered")
 
