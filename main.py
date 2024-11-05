from functions import Bankingapp

app = Bankingapp()
while True:
    print("\n=== Welcome to the Bank ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        app.create_account()
    elif choice == '2':
        app.deposit()
    elif choice == '3':
        app.withdraw()
    elif choice == '4':
        app.transfer()
    elif choice == '5':
        app.check_balance()
    elif choice == '6':
        print("Thank you for using our banking services!")
        break
    else:
        print("Invalid option. Please try again.")