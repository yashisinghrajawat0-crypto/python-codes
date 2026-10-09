age = int(input("Enter your age: "))

if age >= 18:
    print("Age eligible.")
    test = input("Have you passed the driving test? (yes/no): ").lower()

    if test == "yes":
        print("License can be ISSUED. Congratulations!")
    else:
        print("License CANNOT be issued. You need to pass the driving test.")

else:
    print(f"License CANNOT be issued. You are only {age} years old. Minimum age is 18.")