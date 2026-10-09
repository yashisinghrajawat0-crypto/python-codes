bill=float(input("enter the bill amount"))
coupon=input("enter coupon cod:")

if bill<500:
    print("coupon cannot be used. bill must be atleat 500.")
else:
    # bill>= 500,so coupon can be checked 
    if coupon == "SAVE 10":
        discount= bill*0.10
        final_bill= bill - discount
        print(f"10% discount applied! You save Rs.{discount}")
        print(f"Final bill: Rs.{final_bill}")
        
    elif coupon == "SAVE 20":
        discount= bill*0.20
        final_bill= bill - discount
        print(f"20% discount applied! You save Rs.{discount}")
        print(f"final bill:Rs.{final_bill}")
        
    else:
        print("invalid coupon.")
