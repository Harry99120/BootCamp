income = float(input("Enter monthly income: "))
emi = float(input("Enter existing EMI: "))
if income < 30000:
    print("Income too low")
elif emi >= 0.4 * income:
    print("High debt burden")
else:
    print("Eligible for loan")