print("""
            Welcome to our banking system.
""")
create_account = int(input("""  
            Account opening charges =  1000 Rs
            Credit =  500 Rs
            Total charges = 1500 Rs
"""))
first_name = input("Enter your first name: ")
last_name = input("Enter you last name:")
cnic = input("Enter you CNIC number: ")
phone_num = input("Enter your phone number: ")
gender = input("Enter gender (Male/female): ").lower()
while gender not in ['male', 'female']:
    print("""
    ERROR! Please choose a Valid gender (Male/Female)
    """)
    gender = input("Enter gender Male/female: ").lower()
address = input("Enter you address: ")
city = input("Enter your city name: ")
acc_type = input("Enter account type (Saving/Current): ").lower()
while acc_type not in ['current', 'saving']:
    print("""
    ERROR! Please enter Valid account type
    """)
    acc_type = input("Enter account type (Saving/Current): ").lower()
credit = 500
print("Options")
print("1. Withdraw money")
print("2. Deposit money")
choice = input("Enter your choice: ")
if choice == '1':
    print("Enter the amount of money you want to withdraw")
    amount = float(input("Enter amount: "))
    if amount > credit:
        print("Insufficient Balance ")
    else:
        credit -= amount
        print(f"Your current balance is {credit} ")
if choice == '2':
    print("Enter the amount of money you want to deposit")
    amount = float(input("Enter amount: "))
    credit += amount
    print(f"Your current balance is {credit}")
