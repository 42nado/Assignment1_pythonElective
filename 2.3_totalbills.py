
totalbills=float(input("Enter total bills: "))

if totalbills>=20000:
    discount=totalbills*15/100
    netpay=totalbills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))
elif totalbills>=15000:
    discount=totalbills*10/100
    netpay=totalbills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))
elif totalbills>=10000:
    discount=totalbills*5/100
    netpay=totalbills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))
else:
    discount=0
    netpay=totalbills-discount
    print("Discount : " +str(discount))
    print("Netpay : " + str(netpay))