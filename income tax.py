income=float(input("enter your total anual incomen(in rupees)"))
if income<=250000:
    tax=0.0
elif income<=500000:
    tax=(income-250000)*0.05
elif income<=1000000:
    tax= 12500+ (income-500000)*0.20
else:
    tax=112500 + (income-1000000)*0.30
print("calculated income tax:rupees",tax)