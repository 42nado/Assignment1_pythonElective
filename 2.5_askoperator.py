
fnum=int(input("Enter first number :"))
snum=int(input("Enter Second number : "))
operator=input("Operator (+ - * / ) \nSelect operator: ")

if operator=="+":
    result=fnum+snum
    print("Result: ",result)
elif operator=="-":
    result=fnum-snum
    print("Result: ",result)
elif operator=="*":
    result=fnum*snum
    print("Result: ",result)
elif operator=="/":
    result=fnum/snum
    print("Result: ",result)
else:
    print("Invalid input")