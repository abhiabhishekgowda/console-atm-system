import os
import json
from datetime import datetime

filename = "user.json"

# ------------------- Account Loading & Saving -------------------

def load_accounts():
    """Load accounts from JSON file, or create default if empty."""
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as f:
            return json.load(f)   
    else:
        return {
            "sam": {"balance": 27000, "pin": "2136", "history": []},
            "manya": {"balance": 80000.0, "pin": '9972', "history": []},
            "kavya":{"balance": 170000.0, "pin": '7488', "history": []},
        }

def save_accounts(accounts):
    """Save accounts dictionary to JSON file."""
    with open(filename, "w") as f:
        json.dump(accounts, f, indent=4)   

# ------------------- Utility Functions -------------------

def log_transaction(account, message):
    """Append a timestamped transaction message to account history."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    account['history'].append(f"{now}: {message}")

def show_balance(account):
    """Display current balance."""
    print(f"Current Balance: {account['balance']:,.2f}")

# ------------------- ATM Operations -------------------

def deposit(account):
    """Deposit money into account."""
    try:
        amount = int(input("Enter deposit: "))
        if amount >= 0:
            account['balance'] += amount
            log_transaction(account, f"Deposit: ${amount:,.2f}")
            print("Deposit successful.")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Invalid input. Try again!")

def withdraw(account, daily_limit):
    """Withdraw money with daily limit check."""
    try:
        amount = int(input("Enter withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > account['balance']:
            print("Insufficient funds.")
        elif daily_limit + amount > 25000:
            print("You crossed the daily limit of $25,000.")
        else:
            account['balance'] -= amount
            log_transaction(account, f"Withdraw: ${amount:,.2f}")
            print("Withdraw successful.")
            return daily_limit + amount
    except ValueError:
        print("Invalid input. Try again!")
    return daily_limit

def show_history(account):
    """Show transaction history."""
    if not account['history']:
        print("No transactions yet.")
    else:
        print("\n--- YOUR TRANSACTION HISTORY ---")
        for entry in account['history']:
            print(entry)

def change_pin(account):
    """Change account PIN."""
    new_pin = input("Enter new 4-digit PIN: ")
    if new_pin.isdigit() and len(new_pin) == 4:
        account['pin'] = new_pin
        print("PIN updated successfully.")
    else:
        print("PIN must be 4 digits.")

def transfer(accounts, sender_name):
    """Transfer money between accounts."""
    recipient = input("Enter recipient name: ").lower().strip()
    if recipient not in accounts:
        print("Recipient not found.")
    elif recipient == sender_name:
        print("You can't transfer to yourself.")
    else:
        try:
            amount = float(input("Enter transfer amount: "))
            if amount <= 0:
                print("Invalid amount.")
            elif amount > accounts[sender_name]['balance']:
                print("Insufficient funds.")
            else:
                accounts[sender_name]['balance'] -= amount
                accounts[recipient]['balance'] += amount
                log_transaction(accounts[sender_name], f"Transfer: ${amount:,.2f} to {recipient}")
                log_transaction(accounts[recipient], f"Received: ${amount:,.2f} from {sender_name}")
                print("Transfer successful.")
        except ValueError:
            print("Invalid input. Try again!")

# ------------------- ATM Session -------------------

def atm_session(accounts, name):
    """Run ATM session for a user."""
    print(f"Welcome, {name.capitalize()}")
    daily_limit = 0.0
    is_running = True

    while is_running:
        print("\n--- ATM SESSION ---")
        print("1. Balance | 2. Deposit | 3. Withdraw | 4. History | 5. Change PIN | 6. Transfer | 7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number (1-7)!")
            continue

        if choice == 1:
            show_balance(accounts[name])
        elif choice == 2:
            deposit(accounts[name])
        elif choice == 3:
            daily_limit = withdraw(accounts[name], daily_limit)   
        elif choice == 4:
            show_history(accounts[name])
        elif choice == 5:
            change_pin(accounts[name])
        elif choice == 6:
            transfer(accounts, name)
        elif choice == 7:
            save_accounts(accounts)
            print("Goodbye! Data saved.")
            is_running = False
        else:
            print("Invalid choice. Please select 1-7.")

# ------------------- Main Program -------------------

def main():
    accounts = load_accounts()
    print("-- WELCOME TO SOFTBANK --")
    name = input("Enter your name: ").lower().strip()

    if name in accounts:
        attempt = 3
        while attempt > 0:
            user_pin = input("Enter your PIN: ")
            if user_pin == accounts[name]['pin']:
                atm_session(accounts, name)
                break
            else:
                attempt -= 1
                print(f"WRONG PIN. You have {attempt} attempt(s) left.")
    else:
        new_user = input("Name not found. Create new account? (y/n): ").lower()
        if new_user == "y":
            pin = input("Enter your new 4-digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                try:
                    deposit_amount = int(input("Enter initial deposit: "))
                    if deposit_amount >= 0:
                        accounts[name] = {
                            "balance": deposit_amount,
                            "pin": pin,
                            "history": [f"Account created with ${deposit_amount:,.2f}"]
                        }
                        save_accounts(accounts)
                        print("\nAccount successfully created!")
                        print(f"Name: {name.capitalize()}\nBalance: ${deposit_amount:,.2f}")
                    else:
                        print("Invalid deposit amount.")
                except ValueError:
                    print("Please enter a valid number for the deposit.")
            else:
                print("Invalid PIN! Must be 4 digits.")
        else:
            print("Exit...")

if __name__ == "__main__":
    main()






        

            

        









                        


                        














    




    


