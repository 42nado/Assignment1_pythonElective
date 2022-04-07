
bills=float(input("Enter total bills: "))
paymentmode=int(input("Payment mode: \n1. Credit Card\n2. Debit Card\n3. Netbanking\n4. Other payment\nEnter payment mode: "))
if paymentmode==1:
    discount=bills*10/100
    netpay=bills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))
elif paymentmode==2:
    discount=bills*5/100
    netpay=bills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))
elif paymentmode==3:
    discount=bills*2/100
    netpay=bills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))
elif paymentmode==4:
    discount=0
    netpay=bills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))
else:
    print("Invalid input")