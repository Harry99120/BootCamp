print("----- Simple Unit Converter -----")
print("1. Kilometers to Metres")
print("2. Kilometers to Miles")
print("3. Miles to Kilometers")
print("4. Centimeters to Inches")
print("5. Inches to Centimeters")
print("5. Kilogram to Miligram ")
print("-----------------------------")

choice = input("Choose Your Option---> ")

if choice in ['1', '2', '3', '4']:
    number = float(input("Enter the number you want to convert--> "))

    if choice == '1':
        result = number * 1000
        print(f"{number} kilometers is {result} metres.")

    elif choice == '2':
        result = number * 0.621371
        print(f"{number} kilometers is {result} miles.")
        
    elif choice == '3':
        result = number / 0.621371
        print(f"{number} miles is {result} kilometers.")
        
    elif choice == '4':
        result = number / 2.54
        print(f"{number} centimeters is {result} inches.")
        
    elif choice == '5':
        result = number * 2.54
        print(f"{number} inches is {result} centimeters.")

    elif choice == '6':
        result = number * 1000
        print(f"{number} Kilograms is {result} Miligram.")

else:
    print("Invalid Input")