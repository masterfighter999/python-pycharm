#sum of all numbers from 1 to 100 which are divisible by 3 but not divisible by 5.
sum=0
for i in range(3,100,3):
    if i%5!=0:
        sum+=i
        print(i)
print(sum)