balance = 10000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Your Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter deposit amount: "))
        balance += amt
        print("Amount Deposited")

    elif choice == 3:
        amt = int(input("Enter withdrawal amount: "))
        if amt <= balance:
            balance -= amt
            print("Please collect cash")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")