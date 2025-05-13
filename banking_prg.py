def show_balance(balance):
    print(f"\n💰 Your current balance is: ${balance:.2f}\n")


def deposit():
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("❌ Invalid deposit amount. Must be greater than 0.\n")
            return 0
        else:
            print(f"✅ Successfully deposited ${amount:.2f}\n")
            return amount
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return 0


def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.\n")
            return 0
        elif amount > balance:
            print("❌ Insufficient balance. Try a smaller amount.\n")
            return 0
        else:
            print(f"✅ Successfully withdrew ${amount:.2f}\n")
            return amount
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return 0


def main():
    balance = 0.0
    is_running = True

    print("💻 WELCOME TO PYTHON BANK 💻\n")

    while is_running:
        print("------ MENU ------")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("\n👋 Thank you for using Python Bank. Have a great day!")
            is_running = False
        else:
            print("❌ Invalid choice. Please select from 1 to 4.\n")


if __name__ == "__main__":
    main()
