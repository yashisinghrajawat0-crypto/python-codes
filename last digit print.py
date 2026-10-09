num = int(input("Enter a number: "))
num = abs(num)  # handles negative numbers

second_last_digit = (num // 10) % 10
print("Second last digit:", second_last_digit)