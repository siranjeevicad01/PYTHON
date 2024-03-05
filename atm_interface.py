class User:
    def __init__(self, card_number, pin, name):
        self.card_number = card_number
        self.pin = pin
        self.name = name

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

class ATM:
    def __init__(self, users, accounts):
        self.users = users
        self.accounts = accounts
        self.current_user = None

    def login(self):
        card_number = input("Please insert your debit card: ")
        pin = input("Enter your PIN number: ")

        for user in self.users:
            if user.card_number == card_number:
                if user.pin == pin:
                    self.current_user = user
                    print(f"Welcome, {user.name}!")
                    return True
                else:
                    print("Invalid PIN. Please try again.")
                    return False

        print("Card number not recognized. Please try again.")
        return False

    def display_account_information(self):
        if self.current_user:
            account = self.accounts[self.current_user.card_number]
            print("\nAccount Information:")
            print("Account Holder:", self.current_user.name)
            print("Card Number:", self.current_user.card_number)
            print("Balance:", account.balance)
            print("Transaction History:")
            for transaction in account.transaction_history:
                print(transaction)
        else:
            print("Please login first to view account information.")

    def deposit(self, amount):
        if self.current_user:
            account = self.accounts[self.current_user.card_number]
            account.balance += amount
            account.transaction_history.append(f"Deposited: +{amount}")
            print("Deposit successful.")
            print("Updated balance:", account.balance)
        else:
            print("Please login first to perform transactions.")

    def withdraw(self, amount):
        if self.current_user:
            account = self.accounts[self.current_user.card_number]
            if amount <= account.balance:
                account.balance -= amount
                account.transaction_history.append(f"Withdrew: -{amount}")
                print("Withdrawal successful.")
                print("Remaining balance:", account.balance)
            else:
                print("Insufficient funds!")
        else:
            print("Please login first to perform transactions.")

    def transfer(self, amount, recipient_card_number):
        if self.current_user:
            sender_account = self.accounts[self.current_user.card_number]
            recipient_account = self.accounts.get(recipient_card_number)

            if recipient_account:
                if amount <= sender_account.balance:
                    sender_account.balance -= amount
                    recipient_account.balance += amount
                    sender_name = self.current_user.name
                    recipient_name = [user.name for user in self.users if user.card_number == recipient_card_number][0]
                    print("Transfer successful.")
                    print(f"Rs. {amount} transferred from {sender_name} to {recipient_name}.")
                    sender_account.transaction_history.append(f"Transferred Rs.{amount} to {recipient_name}")
                    recipient_account.transaction_history.append(f"Received Rs.{amount} from {sender_name}")
                else:
                    print("Insufficient funds!")
            else:
                print("Recipient account not found.")
        else:
            print("Please login first to perform transactions.")

    def quit(self):
        print("Thank you for using the ATM. Goodbye!")
        exit()

def main():
    # Create user accounts with permanent PINs and names
    users = [User("6383685553", "1234", "Siranjeevi"), User("9876543210", "4321", "Jemi")]

    # Create accounts with initial balance, defaulting to specified amounts
    accounts = {user.card_number: Account(user.card_number, 1500 if user.name == "siranjeevi" else 1000) for user in users}

    # Create ATM instance
    atm = ATM(users, accounts)

    # Prompt user to log in
    while not atm.current_user:
        atm.login()

    # Once logged in, present ATM options
    while True:
        print("\nPlease choose from one of the following options...")
        print("1. Display Account Information")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.display_account_information()
        elif choice == "2":
            amount = float(input("How much Rs would you like to deposit: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("How much Rs would you like to withdraw: "))
            atm.withdraw(amount)
        elif choice == "4":
            amount = float(input("Enter amount to transfer: "))
            recipient_card_number = input("Enter recipient card number: ")
            atm.transfer(amount, recipient_card_number)
        elif choice == "5":
            atm.quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
