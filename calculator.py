# Simple Calculator using if-else

# Step 1: Take numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Choose operation
print("\nChoose operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

op = input("Enter your operation (+, -, *, /): ")

# Step 3: Calculation using if-else
if op == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif op == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif op == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error! Cannot divide by zero.")

else:
    print("Invalid operation! Please use only +, -, *, /.")
