#Calculator in Python
print ("What operation do you want to perform: ")
operator = input("Please enter either +, _, *, / :")
n1 =  float(input("Enter first Number: "))
n2 = float(input ("Enter second Number: "))
if operator == "+":
    print(n1, operator, n2, "=", n1+n2 )          
elif operator == "-":
    print(n1, operator, n2, "=", n1-n2)         
elif operator == '*':
    print(n1, operator, n2, "=", n1*n2)
elif operator == "/":
    print(n1, operator, n2, "=", n1/n2)
else:
    print("Invalid Operator...")          
