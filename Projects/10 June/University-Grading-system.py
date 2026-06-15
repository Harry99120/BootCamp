def get_grade(percentage):
    if percentage >= 90:
        return "A+", 10.0
    elif percentage >= 85:
        return "A", 9.0
    elif percentage >= 80:
        return "A-", 8.5
    elif percentage >= 75:
        return "B+", 8.0
    elif percentage >= 70:
        return "B", 7.0
    elif percentage >= 65:
        return "B-", 6.5
    elif percentage >= 60:
        return "C+", 6.0
    elif percentage >= 55:
        return "C", 5.0
    elif percentage >= 50:
        return "C-", 4.5
    elif percentage >= 45:
        return "D", 4.0
    elif percentage >= 40:
        return "E", 3.0
    else:
        return "F", 0.0


def get_classification(cgpa):
    if cgpa >= 9.0:
        return "Outstanding"
    elif cgpa >= 8.0:
        return "Excellent"
    elif cgpa >= 7.0:
        return "Very Good"
    elif cgpa >= 6.0:
        return "Good"
    elif cgpa >= 5.0:
        return "Satisfactory"
    elif cgpa >= 4.0:
        return "Pass"
    else:
        return "Fail"


print("=" * 50)
print("UNIVERSITY GRADING SYSTEM")
print("=" * 50)

student_name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

num_subjects = int(input("Enter Number of Subjects: "))

total_credits = 0
weighted_grade_points = 0

print("\nEnter Subject Details")

for i in range(num_subjects):
    print(f"\nSubject {i+1}")

    subject = input("Subject Name: ")
    credits = int(input("Credits: "))
    marks = float(input("Percentage Marks: "))

    grade, grade_point = get_grade(marks)

    print(f"Grade       : {grade}")
    print(f"Grade Point : {grade_point}")

    total_credits += credits
    weighted_grade_points += credits * grade_point

# CGPA Calculation
cgpa = weighted_grade_points / total_credits

classification = get_classification(cgpa)

print("\n" + "=" * 50)
print("FINAL RESULT")
print("=" * 50)

print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_no}")
print(f"CGPA         : {cgpa:.2f}")
print(f"Classification: {classification}")

if cgpa >= 4.0:
    print("Status       : PASS")
else:
    print("Status       : FAIL")

print("=" * 50)