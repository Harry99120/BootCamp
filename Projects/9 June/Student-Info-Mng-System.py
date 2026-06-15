
# 1. Accept user input and apply type conversion
name = input("Enter Student Name--> ")
roll_number = input("Enter Roll Number--> ")
age = int(input("Enter Age--> "))
program = input("Enter Program--> ")
cgpa = float(input("Enter CGPA--> "))
completed_courses = int(input("Enter Number of Completed Courses--> "))

# 2. Calculate remaining courses and completion percentage
TOTAL_COURSES = 40
remaining_courses = TOTAL_COURSES - completed_courses
completion_percentage = (completed_courses / TOTAL_COURSES) * 100

# Extension: Determine scholarship eligibility
if cgpa >= 8.5:
    scholarship_status = "Eligible"
else:
    scholarship_status = "Not Eligible"

# 3. Display the formatted report using f-strings
print("\n========== STUDENT REPORT ==========")
print(f"Name                : {name}")
print(f"Roll Number         : {roll_number}")
print(f"Age                 : {age}")
print(f"Program             : {program}")
print(f"CGPA                : {cgpa}")
print(f"Completed Courses   : {completed_courses}")
print(f"Remaining Courses   : {remaining_courses}")
# The :.1f formats the percentage to 1 decimal place, matching the sample output
print(f"Degree Completion   : {completion_percentage:.1f}%")
print("====================================")

# Display Extension Results
print("Extension")
print("Add scholarship eligibility:")
print(f"Scholarship Status  : {scholarship_status}")