num=int(input("Enter the number of terms"))
a=0
b=1
result=0

if num<=0:
    print("Error")
elif num==1:
    print(result)
else:
    for i in range(num):
        print(" ",a)
        result+=a
        a,b=b,a+b