# Python Banking Program with Yellow Output

def yellow_text(text):
    return f"\033[33m{text}\033[0m"

def show_balance(balance):
    print(yellow_text("********************"))
    print(yellow_text(f"Your balance is ${balance:.2f}"))
    print(yellow_text("********************"))

def deposit():
    print(yellow_text("********************"))
    amount = float(input(yellow_text("Enter an amount to be deposited: ")))
    print(yellow_text("********************"))

    if amount < 0:
        print(yellow_text("********************"))
        print(yellow_text("That's not a valid amount"))
        print(yellow_text("********************"))
        return 0
    else:
        return amount

def withdraw(balance):
    print(yellow_text("********************"))
    amount = float(input(yellow_text("Enter amount to be withdrawn: ")))
    print(yellow_text("********************"))

    if amount > balance:
        print(yellow_text("********************"))
        print(yellow_text("Insufficient funds"))
        print(yellow_text("********************"))
        return 0
    elif amount < 0:
        print(yellow_text("********************"))
        print(yellow_text("Amount must be greater than 0"))
        print(yellow_text("********************"))
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print(yellow_text("********************"))
        print(yellow_text("   Banking Program  "))
        print(yellow_text("********************"))
        print(yellow_text("1. Show Balance"))
        print(yellow_text("2. Deposit"))
        print(yellow_text("3. Withdraw"))
        print(yellow_text("4. Exit"))
        print(yellow_text("********************"))
        choice = input(yellow_text("Enter Your choice (1-4): "))

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print(yellow_text("********************"))
            print(yellow_text("That is not a valid choice"))
            print(yellow_text("********************"))

    print(yellow_text("********************"))
    print(yellow_text("Thank you! Have a nice day!"))
    print(yellow_text("********************"))

if __name__ == '__main__':
    main()
