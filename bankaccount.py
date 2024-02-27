import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.date_of_opening = datetime.date.today()
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        else:
            return "Invalid amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        elif amount <= 0:
            return "Invalid amount"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}\nAccount Number: {self.account_number}\nDate of Opening: {self.date_of_opening}\nBalance: {self.balance}")


def main():
    account_number = input("Enter account number: ")
    customer_name = input("Enter customer name: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, customer_name, initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Customer details")
        print("5. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            print(f"Amount deposited: {account.deposit(amount)}")
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            result = account.withdraw(amount)
            print(result)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            account.customer_details()
        elif choice == 5:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
