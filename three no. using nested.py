a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "is the greatest")
    else:
        print(c, "is the greatest")
else:
    if b > c:
        print(b, "is the greatest")
    else:
        print(c, "is the greatest")