a=float(input("enter the  number: "))
if a>=0 and a<10000.0:
    print("INCOME TAX IS RUPEE 0")
elif a>=10000.0 and a<25000.0:
    print("INCOME TAX IS RUPEES",0.1*a)
elif a>=25000.0 and a<50000.0:
    print("INCOME TAX IS RUPEES",0.2*a)
elif a>=50000.0:
    print("INCOME TAX IS RUPEES ",0.3*a)
else:
    print("INVALID INCOME")