age = int(input("Enter age: "))
degree = input("Enter degree (B.Tech/MCA): ")
cgpa = float(input("Enter CGPA: "))
if 21 <= age <= 40:
    if degree == "B.Tech" or degree == "MCA":
        if cgpa >= 7.0:
            print("Interview Shortlisted")
        else:
            print("Rejected: CGPA below 7.0")
    else:
        print("Rejected: Invalid degree")
else:
    print("Rejected: Age not between 21 and 40")