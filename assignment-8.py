#Advanced Bank ATM System
pin = "1234" #Default pin
balance = 1000.00 #Default balance
transaction_history = []


def menu():
    print('''    1. Check Balance
     2. Deposit Money 
     3. Withdraw Money
     4. View Transaction History
     5. Exit System''')

def validate_pin():
    for attempt in range (5, 0, -1):
        input_pin = input("Enter your 4-digit PIN: ")
        if input_pin == pin:
            print("PIN successfully verified")
            return True
        else:
            print(f"Incorrect PIN. {attempt - 1} attempts left")
            if attempt - 1 == 0:
                print("Access denied. Too many incorrect attempts.\nExiting System")
                break
        

def check_balance():
    print(f"Your current balance is {balance:.2f}")


def deposit_money():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposit - {amount:.2f}")
            print(f"{amount:.2f} successfully deposited in your account.\nYour current balance is  {balance + amount:.2f} ")
        else:
            print("Amount must be positive")
    except ValueError:
        print("Invalid input! Please enter a valid amount")


def withdraw_money():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount >= balance:
            print("Error.Insufficient Funds")
        elif amount < balance:
            balance -= amount
            transaction_history.append(f"Withdrawal - {amount:.2f}")
            print(f"{amount:.2f} was withdrawn from your account. Your remaining balance is {balance - amount:.2f}")
    except ValueError:
        print("Invalid Input! Enter a valid amount")        
    

def check_history():
    print("Transaction History:")   
    if transaction_history:
        for transactions in transaction_history:
            print(transactions) 
    else:
        print("No transactions available")


print("Welcome to Lavender ATM System")  
validate_pin()

while True:
    
    menu()

    choice = input("Enter an option from 1-5: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit_money()    
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_history()
    elif choice == "5":
        print("Goodbye! Exiting Lavender ATM system...")
        break                      
      

    else:
        print("Invalid input! Enter a valid option")
