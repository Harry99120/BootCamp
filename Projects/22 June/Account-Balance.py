class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n✨ Success: Deposited ${amount:.2f}")
            print(f"💰 Current Balance: ${self.balance:.2f}")
        else:
            print("\n❌ Error: Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n❌ Error: Invalid withdrawal amount.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"\n✨ Success: Withdrew ${amount:.2f}")
            print(f"💰 Current Balance: ${self.balance:.2f}")
        else:
            print(f"\n❌ Error: Insufficient funds. Current Balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"\n💰 Your Current Balance is: ${self.balance:.2f}")


def atm_machine():
    user_account = BankAccount()
    
    print("====================================")
    print("    WELCOME TO THE PY-BANK ATM      ")
    print("====================================")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("\nEnter choice (1-4) and press Enter: ").strip()

        if not choice:
            print("\n⚠️ No input detected. Please type a number first, then press Enter.")
            continue  

        if choice == '1':
            user_account.check_balance()
            
        elif choice == '2':
            try:
                raw_amount = input("Enter amount to deposit: $").strip()
                if raw_amount:
                    user_account.deposit(float(raw_amount))
                else:
                    print("\n❌ Transaction cancelled: No amount entered.")
            except ValueError:
                print("\n❌ Error: Please enter a valid numeric value.")
                
        elif choice == '3':
            try:
                raw_amount = input("Enter amount to withdraw: $").strip()
                if raw_amount:
                    user_account.withdraw(float(raw_amount))
                else:
                    print("\n❌ Transaction cancelled: No amount entered.")
            except ValueError:
                print("\n❌ Error: Please enter a valid numeric value.")
                
        elif choice == '4':
            print("\n====================================")
            print(" Thank you for using Py-Bank ATM! 👋")
            print("====================================")
            break
            
        else:
            print(f"\n❌ Invalid choice '{choice}'! Please type 1, 2, 3, or 4.")

atm_machine()