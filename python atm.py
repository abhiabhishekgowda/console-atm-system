import os
import json
from datetime import datetime

filename = "accounts.json"

# Load or Initialize Data
if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as f:
        accounts = json.load(f)
else:
    accounts = {
        "sam": {"balance": 27000.0, "pin": '2136', "history": []},
        "abhi": {"balance": 30000.0, "pin": '9972', "history": []},
        "manya": {"balance": 80000.0, "pin": '2136', "history": []}
    }

print("-- WELCOME TO SOFTBANK --")
name = input("Enter your name: ").lower().strip()

if name in accounts:
    attempts = 3
    while attempts > 0:
        user_pin = input("Enter your pin: ")
        if user_pin == accounts[name]['pin']:
            print(f"Welcome, {name.capitalize()}")
            
            is_running = True
            daily_limit = 0.0
            
            while is_running:
                print("\n--- ATM SESSION ---")
                print("1. Balance | 2. Deposit | 3. Withdraw | 4. History | 5. Change PIN | 6. Transfer | 7. Exit")

                try:
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Please enter a valid number (1-7)!")
                    continue

                # 1. BALANCE
                if choice == 1:
                    print(f"Current Balance: ${accounts[name]['balance']:,.2f}")

                # 2. DEPOSIT
                elif choice == 2:
                    try:
                        deposit = float(input("Enter deposit amount: "))
                        if deposit > 0:
                            accounts[name]['balance'] += deposit
                            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            accounts[name]['history'].append(f"{now}: Deposit ${deposit:,.2f}")
                            print("Deposit Success!")
                        else:
                            print("Invalid amount.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                # 3. WITHDRAW
                elif choice == 3:
                    try:
                        withdraw = float(input("Enter withdrawal amount: "))
                        if withdraw <= 0:
                            print("Invalid amount.")
                        elif withdraw > accounts[name]['balance']:
                            print("Insufficient funds.")
                        elif daily_limit + withdraw > 25000:
                            print("Daily limit exceeded! Max $25,000 per session.")
                        else:
                            accounts[name]['balance'] -= withdraw
                            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            accounts[name]['history'].append(f"{now}: Withdraw ${withdraw:,.2f}")
                            daily_limit += withdraw
                            print("Withdrawal Success!")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                # 4. HISTORY
                elif choice == 4:
                    if not accounts[name]['history']:
                        print("No transactions yet.")
                    else:
                        print("\n--- Transaction History ---")
                        for entry in accounts[name]['history']:
                            print(entry)

                # 5. CHANGE PIN
                elif choice == 5:
                    new_pin = input("New 4-digit PIN: ")
                    if new_pin.isdigit() and len(new_pin) == 4:
                        accounts[name]['pin'] = new_pin
                        print("PIN Updated!")
                    else:
                        print("Invalid PIN! Must be a 4-digit number.")

                # 6. TRANSFER (Fixed the %s error here)
                elif choice == 6:
                    recipient = input("Enter recipient name: ").lower().strip()
                    if recipient not in accounts:
                        print("Recipient not found.")
                    elif recipient == name:
                        print("You cannot transfer to yourself.")
                    else:
                        try:
                            amount = float(input("Enter transfer amount: "))
                            if amount <= 0:
                                print("Invalid amount.")
                            elif amount > accounts[name]['balance']:
                                print("Insufficient funds.")
                            else:
                                accounts[name]['balance'] -= amount
                                accounts[recipient]['balance'] += amount
                                
                                # Use standard format codes: %Y-%m-%d %H:%M:%S
                                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                
                                accounts[name]['history'].append(f"{now}: Transferred ${amount:,.2f} to {recipient}")
                                accounts[recipient]['history'].append(f"{now}: Received ${amount:,.2f} from {name}")
                                print(f"Successfully transferred ${amount:,.2f} to {recipient}")
                        except ValueError:
                            print("Invalid input. Please enter a numeric amount.")

                # 7. EXIT & SAVE
                elif choice == 7:
                    with open(filename, "w") as f:
                        json.dump(accounts, f, indent=4)
                    is_running = False
                    print("Goodbye! Data saved.")

                else:
                    print("Invalid choice. Please select 1-7.")

            break # Exit the attempts while-loop
        else:
            attempts -= 1
            print(f"WRONG PIN. You have {attempts} attempt(s) left.")
            
    if attempts == 0:
        print("Your account access has been blocked for this session.")

# NEW USER REGISTRATION
else:
    new_user = input("Name not found. Create new account? (y/n): ").lower()
    if new_user == "y":
        pin = input("Enter your new 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                if initial_deposit >= 0:
                    accounts[name] = {
                        "balance": initial_deposit,
                        "pin": pin,
                        "history": [f"Account created with ${initial_deposit:,.2f}"]
                    }
                    with open(filename, "w") as f:
                        json.dump(accounts, f, indent=4)
                    print("\nAccount successfully created!")
                    print(f"Name: {name.capitalize()}\nBalance: ${initial_deposit:,.2f}")
                else:
                    print("Invalid deposit amount.")
            except ValueError:
                print("Please enter a valid number for the deposit.")
        else:
            print("Invalid PIN! Must be 4 digits.")
    else:
        print("Exit...")











                        


                        














    




    


