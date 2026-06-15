monthly_budget = float(input("Enter Your Monthly Budget-->"))
food_expense = float(input("Enter Food Expense-->"))
travel_expense =  float(input("Enter Travel Expense-->"))
internet_bill =  float(input("Enter Internet Expense-->"))
entertainment_expense =  float(input("Enter Entertainment Expense-->"))
miscellaneous_expense =  float(input("Enter Miscellaneous Expense-->"))
total_expense = food_expense + travel_expense + internet_bill + entertainment_expense + miscellaneous_expense

Balance_Left = monthly_budget - total_expense 
Percentage_Spent = (total_expense / monthly_budget ) * 100 

# Output 
print("\n========== EXPENSE TRACKER ==========")
print(f"Monthly Budget : {monthly_budget }" )
print(f"Balance Left : {Balance_Left}" )
print(f"Percentage Of Money Spent : {Percentage_Spent}" )