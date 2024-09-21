b=1000
a=int(input("Enter the number of occupants : "))
if a==1:
    occupancy_charge = 0*b
if a==2:
    occupancy_charge = 0.2*b
if a==3:
    occupancy_charge=0.3*b
v=input("Enter the type of view (S/G/D) ")
if v=='S':
    charge= 0.25*b
if v=='G':
    charge=0.1*b
if v=='D':
    charge = 0*b
rate= b+occupancy_charge+charge
duration=int(input("Enter the no. of days of occupancy : "))
final_charge= duration*rate
bill_amount= final_charge*0.1+final_charge
print("The final bill amount is : ", bill_amount)
