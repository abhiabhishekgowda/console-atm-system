print("---WELCOME TO THE COMMUNITY BANK---")

accounts = {
    "sam": {"balance": 27000, "pin": '2136', "history": []},
    "abhi": {"balance": 30000, "pin": '9972', "history": []},
    "manya": {"balance": 80000, "pin": '2136', "history": []}
}

# CHECK IF THE NAME EXISTS IN OUR DATABASE
name = input("Enter your name: ").lower().strip()
if name in accounts:
    attempts = 3
    while attempts > 0:
        enter_pin = input("Enter your PIN: ")
        if enter_pin == accounts[name]["pin"]:
            print(f"Welcome, {name}!")

            is_running = True
            daily_limit = 0
            while is_running:

                print(f"\n---{name}'s SESSION---")
                print("1. Balance | 2. Deposit | 3. Withdraw | 4. Check History | 5. Exit")
                try:
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Please enter a number!")
                    continue
            
                if choice == 1:
                    print(f"Your balance is: {accounts[name]['balance']}")
            
                elif choice == 2:
                    try:
                        deposit = int(input("Enter deposit amount: "))
                        if deposit > 0:
                            accounts[name]['balance'] += deposit
                            accounts[name]['history'].append(f"Deposited {deposit}")
                            print("Deposit successful!")
                        else:
                            print("Invalid amount!")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            
                elif choice == 3:
                    try:
                        withdraw = int(input("Enter withdrawal amount: "))
                        if withdraw <= 0:
                            print("Invalid amount!")
                        elif withdraw > accounts[name]['balance']:
                            print("Insufficient funds!")
                        elif daily_limit + withdraw > 15000:
                            print("Daily withdrawal limit exceeded!(15000)")
                        else:
                            accounts[name]['balance'] -= withdraw
                            accounts[name]['history'].append(f"Withdrew {withdraw}")
                            daily_limit += withdraw
                            print("Withdrawal successful!")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            
                elif choice == 4:
                    print("Your transaction history:")
                    for h in accounts[name]['history']:
                        print("-", h)
            
                elif choice == 5:
                    print("Exiting... Thank you!")
                    is_running = False
            
                else:
                    print("Invalid choice, try again.")
            break
        else:
            attempts -= 1
            print(f"Wrong PIN. Attempts left: {attempts}")
    if attempts == 0:
        print("Account blocked due to too many failed attempts.")
else:
    print("Name not found in database.")
                    




    


