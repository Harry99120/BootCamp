# Initial balance and a list that includes the starting balance
balance = 1000.00
transaction_history = ["Initial balance: 1000.00"]

def check_balance():
    print(f"\nYour current balance is: {balance:.2f}")

def deposit_money():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid input! Deposit amount must be greater than zero.")
            return
        
        balance += amount
        record = f"Deposited: {amount:.2f}"
        transaction_history.append(record)
        print(f"Successfully deposited {amount:.2f} (Current Balance: {balance:.2f})")
    except ValueError:
        print("Invalid input! Please enter a numerical value.")

def withdraw_money():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid input! Withdrawal amount must be greater than zero.")
            return
        
        if amount > balance:
            print("Transaction Denied! Insufficient balance.")
        else:
            balance -= amount
            # Appending the transaction details AND the running balance to the list
            record = f"Withdrew: {amount:.2f} (Remaining Balance: {balance:.2f})"
            transaction_history.append(record)
            print(f"Successfully withdrew {amount:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numerical value.")

def show_history():
    print("\n--- Transaction History ---")
    if not transaction_history:
        print("No transactions recorded yet.")
    else:
        for record in transaction_history:
            print(record)

def atm_simulation():
    while True:
        print("\n=========================")
        print("     ATM MACHINE SIMULATION     ")
        print("=========================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        match choice:
            case "1":
                check_balance()
            case "2":
                deposit_money()
            case "3":
                withdraw_money()
            case "4":
                show_history()
            case "5":
                print("\nThank you for using our ATM system. Goodbye!")
                break
            case _:
                print("Invalid Choice! Please select a valid option (1-5).")

if __name__ == "__main__":
    atm_simulation()