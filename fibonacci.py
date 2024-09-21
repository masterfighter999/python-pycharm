a,b=1,1
n=int(input("Enter the number of terms : "))
sum=0
average=0.0
if n>0:
    for i in range(n):
        print(a, end=' ')
        sum+=a
        a,b=b,a+b
    avg=sum/n
print()
print(avg)