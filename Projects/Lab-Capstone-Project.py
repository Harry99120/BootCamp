print("--- K.R.M.U Admission Portal ---")
print("Please enter the student's details below.\n")

try:
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    percentage_12th = float(input("Enter Class 12 Percentage (0-100): "))
    entrance_score = float(input("Enter Entrance Exam Score (0-100): "))
    category = input("Enter Category (e.g., General, OBC, SC/ST): ")

    if age <= 0 or percentage_12th < 0 or percentage_12th > 100 or entrance_score < 0 or entrance_score > 100:
        print("\nError: Invalid numerical values. Percentages and scores must be between 0 and 100.")
    
    else:
        is_eligible = False
        if age >= 17 and percentage_12th >= 60.0 and entrance_score >= 50.0:
            is_eligible = True

        scholarship_status = "No Scholarship"
        grade = "N/A"
        overall_score = 0.0

        if is_eligible:
            if percentage_12th >= 90.0:
                scholarship_status = "100% Tuition Waiver"
            elif percentage_12th >= 80.0:
                scholarship_status = "50% Tuition Waiver"
            
            overall_score = (percentage_12th + entrance_score) / 2
            
            if overall_score >= 85:
                grade = "A+"
            elif overall_score >= 75:
                grade = "A"
            elif overall_score >= 60:
                grade = "B"
            else:
                grade = "C"

        print("\n========== ADMISSION REPORT ==========")
        print(f"Date                : 24 February 2026")
        print(f"Name                : {name}")
        print(f"Age                 : {age}")
        print(f"Category            : {category}")
        print(f"Class 12 %          : {percentage_12th}%")
        print(f"Entrance Score      : {entrance_score}")
        print("--------------------------------------")
        
        if is_eligible:
            print("Eligibility         : ELIGIBLE")
            print(f"Admission Grade     : {grade} (Overall: {overall_score:.1f}%)")
            print(f"Scholarship Status  : {scholarship_status}")
        else:
            print("Eligibility         : NOT ELIGIBLE")
            print("Admission Grade     : N/A")
            print("Scholarship Status  : N/A")
        print("======================================")

except ValueError:
    print("\nSystem Error: Invalid input type. Please enter numbers for Age, Percentage, and Score.")