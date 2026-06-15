Marks = int(input("Enter marks: "))
if Marks >= 40:
    if Marks >= 90:
        print("Distinction")
    elif Marks >= 75:
        print("First Division")
    elif Marks >= 60:
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Fail")