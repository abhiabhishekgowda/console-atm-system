accounts = {
    "Abhishek": 10000,
    "sam": 5000,
    "Student": 500
}

print("--- WELCOME TO THE COMMUNITY BANK ---")
name = input("Enter your name to login: ")

# Check if the name exists in our database
if name in accounts:
    print(f"Login successful! Welcome, {name}.")
    is_running = True
    
    while is_running:
        print(f"\n--- {name}'s SESSION ---")
        print("1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit")
        choice = int(input("Choose: "))

        if choice == 1:
            print(f"Balance: {accounts[name]}")

        elif choice == 2:
            amount = int(input("Deposit: "))
            if amount > 0:
                accounts[name] += amount
                print("Deposit Success!")
            else:
                print("Invalid amount!")

        elif choice == 3:
            amount = int(input("Withdraw: "))
            if 0 < amount <= accounts[name]:
                accounts[name] -= amount
                print("Withdrawal Success!")
            else:
                print("Insufficient funds or invalid amount!")

        elif choice == 4:
            print(f"Logging out {name}")
            is_running = False

        else:
            print("Invalid choice, try again.")
else:
    print("Name not found in database.")

            
                






    


