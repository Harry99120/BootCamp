# ==========================================
# 1. ACCEPT INPUTS (Input/Output & Variables)
# ==========================================
print("--- Enter Student Details ---")
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Taking subject marks and converting them to float (Type Conversion)
print("\n--- Enter Marks (out of 100) ---")
sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

attendance_pct = float(input("\nEnter Attendance Percentage: "))
assignment_score = float(input("Enter Assignment Score (out of 100): "))

# ==========================================
# 2. CALCULATIONS (Operators & Expressions)
# ==========================================

# Academic Percentage
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
academic_percentage = total_marks / 5

# Attendance Status (Control Flow)
if attendance_pct >= 75:
    attendance_status = "Regular"
else:
    attendance_status = "Shortage"

# Internal Assessment Score (Assuming it's based heavily on the assignment)
internal_assessment_score = assignment_score

# Final Performance Score (Assuming equal weight to academics and internal assessment)
final_performance_score = (academic_percentage + internal_assessment_score) / 2

# Grade and Pass/Fail Result Calculation
if final_performance_score >= 90:
    grade = "O (Outstanding)"
    result = "PASS"
elif final_performance_score >= 80:
    grade = "A (Excellent)"
    result = "PASS"
elif final_performance_score >= 70:
    grade = "B (Good)"
    result = "PASS"
elif final_performance_score >= 60:
    grade = "C (Average)"
    result = "PASS"
elif final_performance_score >= 40:
    grade = "D (Pass)"
    result = "PASS"
else:
    grade = "F (Fail)"
    result = "FAIL"

if final_performance_score >= 85 and attendance_pct >= 85:
    scholarship_eligibility = "Eligible"
else:
    scholarship_eligibility = "Not Eligible"

if final_performance_score >= 80:
    rank_category = "Top Tier"
elif final_performance_score >= 60:
    rank_category = "Middle Tier"
else:
    rank_category = "Lower Tier"

if final_performance_score >= 75:
    distinction = "Awarded"
else:
    distinction = "Not Awarded"

# ==========================================
# 3. DISPLAY DASHBOARD (Output Formatting)
# ==========================================
print("\n" + "="*50)
print("           STUDENT PERFORMANCE DASHBOARD")
print("="*50)
print(f"Student Name: {student_name}")
print(f"Roll Number : {roll_number}")
print("-" * 50)

print("Marks Summary:")
print(f"Subject 1: {sub1}")
print(f"Subject 2: {sub2}")
print(f"Subject 3: {sub3}")
print(f"Subject 4: {sub4}")
print(f"Subject 5: {sub5}")
print("-" * 50)

print(f"Academic Average : {academic_percentage}%")
print(f"Assignment Score : {assignment_score}")
print(f"Attendance       : {attendance_pct}%")
print(f"Status           : {attendance_status}")
print("-" * 50)

print(f"Performance Index: {final_performance_score}%")
print(f"Grade            : {grade}")
print(f"Result           : {result}")
print("-" * 50)

print("Bonus Features:")
print(f" • Scholarship Eligibility : {scholarship_eligibility}")
print(f" • Rank Category           : {rank_category}")
print(f" • Distinction Certificate : {distinction}")
print("="*50)