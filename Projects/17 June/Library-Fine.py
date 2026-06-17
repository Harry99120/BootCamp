total_fine_collected = 0
highest_fine = 0
student_count = 0

print("--- Library Fine Calculator ---")

while True:
    name = input("\nEnter Student Name (or type 'exit' to finish): ")

    if name.lower() == 'exit':
        break
        
    days_late = int(input(f"Enter days late for {name}: "))
    
    if days_late <= 0:
        individual_fine = 0
    elif 1 <= days_late <= 5:
        individual_fine = days_late * 5
    elif 6 <= days_late <= 10:
        individual_fine = days_late * 10
    else: 
        individual_fine = days_late * 20

    print(f"Individual Fine for {name}: ₹{individual_fine}")
    
    student_count += 1
    total_fine_collected += individual_fine
    
    if individual_fine > highest_fine:
        highest_fine = individual_fine

print("\n===============================")
print("         FINAL SUMMARY         ")
print("===============================")
print(f"Total Fine Collected: ₹{total_fine_collected}")
print(f"Highest Fine:         ₹{highest_fine}")

if student_count > 0:
    average_fine = total_fine_collected / student_count
    print(f"Average Fine:         ₹{average_fine:.2f}")
else:
    print("Average Fine:         ₹0.00 (No students processed)")