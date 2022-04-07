

number=int(input("Enter a number : "))

if number<0:
    absolute= number*(-1)       #alternative absolute=abs(number)
else:
    absolute=number

print("Absolute value of ", number, " is " ,absolute);