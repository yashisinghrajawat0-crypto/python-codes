# Electricity Bill Calculator

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
    rate = 5
elif units <= 200:
    # First 100 units @ 5, remaining @ 7
    bill = (100 * 5) + (units - 100) * 7
    rate = 7
else:
    # First 100 @ 5, next 100 @ 7, remaining @ 10
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    rate = 10

print(f"Units consumed: {units}")
print(f"Total bill: Rs. {bill}")
