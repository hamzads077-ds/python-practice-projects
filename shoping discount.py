Shopping_amount = float(input("Enter Your shopping amount: "))
if Shopping_amount >= 5000:
    discount = Shopping_amount * 0.10 
    final_amount = Shopping_amount - discount
    print("congratulations You have availed 10% discount") 
    print("Your final bill is:", final_amount)
else:
    print("No discount for you. You have to pay full amount")