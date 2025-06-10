class ATM:
    def init(self, user_pin, user_balance=0):
        self.user_pin = user_pin
        self.balance = user_balance

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")
            if pin == self.user_pin:
                print("Authentication successful.\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts remaining: {attempts}")
        print("Too many failed attempts. Exiting.")
        return False

    def display_menu(self):
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        print(f"\nYour current balance is: ${self.balance:.2f}")

    def deposit(self):
        amount = input("Enter amount to deposit: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive.")
                return
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        except ValueError:
            print("Invalid amount.")

    def withdraw(self):
        amount = input("Enter amount to withdraw: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive.")
                return
            if amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Invalid amount.")

    def run(self):
        if not self.authenticate():
            return
        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Initialize and run the ATM
if name == "main":
    my_atm = ATM(user_pin="1234", user_balance=1000.0)
    my_atm.run()