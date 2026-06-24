class ATM:
    def __init__(self, pin, balance, owner):
        self.__pin = pin
        self.__balance = balance
        self._owner = owner
        self.__authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            return True
        return False

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amt):
        if self.__authenticated:
            self.__balance += amt
        
    def withdraw(self, amt):
        if self.__authenticated and amt <= 20000:
            if amt <= self.__balance:
                self.__balance -= amt
            else:
                print("Insufficient balance")
        else:
            print("Auth failed or limit exceeded")

# Example
atm = ATM(1234, 50000, "Harmeet")
if atm.authenticate(1234):
    atm.withdraw(5000)
    print(f"New Balance: {atm.balance}")