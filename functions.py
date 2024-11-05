account_file = "account.txt"
class Bankingapp:
  def __init__(self):
    self.accounts = self.load_account()
  def is_valid_account_numbr(self,account_number):
    return len(str(account_number)) == 10 and str(account_number).isdigit()

  def load_account(self):
    accounts = {}
    try:
        with open(account_file, 'r') as file:
            for line in file:
                account_number, balance = line.strip().split(",")
                accounts[account_number] = float(balance)
    except FileNotFoundError:
        pass
    return accounts

  def save_account(self):
    with open(account_file, 'w') as file:
        for account_number, balance in self.accounts.items():
            file.write(f"{account_number}, {balance}\n")

  def create_account(self):
    account_number = input("Enter account number:")

    if self.is_valid_account_numbr(account_number):
        if account_number in self.accounts:
            print("already exists")
        else:
           try:
               balance = float(input("Enter deposit ammount"))
               self.accounts[account_number] = balance
               self.save_account()
               print(f"account created successfuly! Balance:{balance}")

           except ValueError:
                print("Invalid amount. please enter a valid number")

    else:
          print("invalid account number. try again")

  def deposit(self):
    account_number = input("Enter your account number:")

    if account_number in self.accounts:
        try:
            amount = float(input("enter amount to deposite:"))
            self.accounts[account_number] += amount
            self.save_account()
            print(f"{amount} deposited. New balance{self.accounts[account_number]}")
        except ValueError:
            print("Invalid amount")
    else:
        print("invalid account no.. create an account")


  def withdraw(self):
    account_number = input("enter your account number: ")

    if account_number in self.accounts:
        try:
            amount = float(input("enter withdraw amount: "))
            if amount <= self.accounts[account_number]:
                self.accounts[account_number] -=amount
                self.save_account()
                print(f"withdrawl amount: {amount} Remaining balance {self.accounts[account_number]}")
            else:
                print("insufficient fund")

        except ValueError:
            print("Invalid amount... please enter a valid number")

    else:
        print("invalid account number")

  def check_balance(self) :
    account_number = input("Enter your account number:")

    if account_number in self.accounts:
        print(f"Your balance is: {self.accounts[account_number]}")
    else:
        print("Account not found")

  def transfer(self):
    sender = input("enter your account number:")
    recipient = input("enter recipient's account number:")

    if sender in self.accounts and recipient in self.accounts:

        try:
            amount = float(input("enter amount to transfer:"))
            if amount <= self.accounts[sender]:
                self.accounts[sender] -= amount
                self.accounts[recipient] +=amount
                self.save_account()
                print(f"tranfer successfull... new balance: {self.accounts[sender]}")

            else:
                print("insufficient fund.")
        except ValueError:
            print("Invalid amount")

    else:
        if sender not in self.accounts:
            print("Sender account not found.")
        if recipient not in self.accounts:
            print("recipient account not found.")

