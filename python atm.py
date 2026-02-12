accounts = {
    "sam": {"balance": 10000, "pin": "2136"},
    "abhi": {"balance": 27000, "pin": "8088"},
    "elon": {"balance": 500, "pin": "8088"} # Fixed: made string
}

def get_amount(prompt):
    """Helper function to handle numeric input and avoid repetition."""
    try:
        amount = int(input(prompt))
        return amount
    except ValueError:
        print(" Invalid input! Please enter a numeric amount.")
        return None

print("--- WELCOME TO THE COMMUNITY BANK ---")
name = input("Enter your name: ").lower().strip()

if name in accounts:
    pin = input("Enter your PIN: ")
    if pin == accounts[name]["pin"]:
        print(f"\n Access Granted. Welcome, {name.capitalize()}!")
        
        while True:
            print(f"\n--- {name.upper()}'S SESSION ---")
            print("1. Balance | 2. Deposit | 3. Withdraw | 4. Exit")
            choice = input("Choice: ")

            if choice == '1':
                print(f" Current Balance: ${accounts[name]['balance']}")

            elif choice == '2':
                amt = get_amount("Enter deposit amount: ")
                if amt is not None and amt > 0:
                    accounts[name]['balance'] += amt
                    print(f" Deposited ${amt}. New balance: ${accounts[name]['balance']}")

            elif choice == '3':
                amt = get_amount("Enter withdrawal amount: ")
                if amt is not None:
                    if 0 < amt <= accounts[name]['balance']:
                        accounts[name]['balance'] -= amt
                        print(f" Withdrew ${amt}. Remaining: ${accounts[name]['balance']}")
                    else:
                        print(" Insufficient funds or invalid amount.")

            elif choice == '4':
                print(" Thank you for using Community Bank. Goodbye!")
                break
            else:
                print(" Invalid choice, please pick 1-4.")
    else:
        print(" Incorrect PIN.")
else:
    print(" User not found.")
            
                






    


