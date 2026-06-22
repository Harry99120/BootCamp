def student_report(name, marks):
    print("\n----- Student Report -----")
    print(f"Name  : {name}")
    print(f"Marks : {marks}")
    print("-" * 26)

def add_bonus(marks):
    marks = marks + 5
    print(f"Inside Function Marks : {marks}")

def sum_marks(n):
    if n <= 1:
        return n
    return n + sum_marks(n - 1)

def square(x):
    return x * x

def cube(x):
    return x ** 3

def apply_operation(func, value):
    return func(value)

student_name = input("Enter Student Name: ")
student_marks = int(input("Enter Marks: "))
student_report(student_name, student_marks)

add_bonus(student_marks)
print(f"Outside Function Marks: {student_marks}") 
print("-" * 26)

rec_num = int(input("\nEnter a number for recursive sum: "))
total_sum = sum_marks(rec_num)
print(f"Recursive Sum = {total_sum}")
print("-" * 26)

print("\nChoose Operation:")
print("1. Square")
print("2. Cube")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    selected_function = square
    val_name = "Square"
elif choice == "2":
    selected_function = cube
    val_name = "Cube"
else:
    print("Invalid choice, defaulting to Square.")
    selected_function = square
    val_name = "Square"

num_to_calculate = int(input(f"Enter a number to {val_name.lower()}: "))
result = apply_operation(selected_function, num_to_calculate)
print(f"Result of {val_name}: {result}")