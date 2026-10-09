balance = 5000  # available account balance
amount = float(input("Enter withdrawal amount: "))

if amount > 0:
    if amount <= balance:
        print("Withdrawal successful!")
        balance = balance - amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")
else:
    print("Invalid amount! Amount must be greater than zero.")