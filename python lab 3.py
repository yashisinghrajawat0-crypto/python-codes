m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("Total Marks =", total)
print("Percentage =", percentage)

if percentage >= 80:
    print("Grade A")
elif percentage >= 70:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Grade E")