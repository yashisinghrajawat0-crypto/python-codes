order=float(input("enter the order amount"))
customer=input("enter the cutomer is (premium or regular):")
if customer=="premium":
    print("premium cutomer: no delivery charges will be apllied", order)
else:
    if order<300:
        print("order amount is less than 300,delivery charger will be applied",order+50)
    elif order>=300 and order<=599:
         print("order amount is btw 300 and 599,delivery charger will be applied",order+30)
    elif order>=600:
             print("order amount is  600 or more, no delivery charger will be applied",order)
    else:
        print("Invalid orde amount")              
                 
      

      
        
    
    