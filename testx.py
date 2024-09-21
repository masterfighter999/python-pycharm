"""students=['teddy','saloni','nikita','john','smith','alice']
print(students[1:6:2])"""

"""n=int(input("Enter the number : "))
for i in range(1,n):
    print(i)"""

"""a_list=[1,2,3,4,7,6]
print(a_list[0:4])
print(a_list[-1:-2])"""

"""a,*b=['john','peter','lucy']
print(a,*b)
print(a)
print(*b)"""

"""stu=[1,2,3,'smith','john',2.4,5.7,[1.5,3]]
for i in stu:
    print(i)
print(stu)
x=stu[-1][0]
print(x)
x=stu[-1][0]=9.99
print(x)"""

"""stu1=['teddy','saloni','nikita','john','frank','ali']
print(stu1)
stu1.append('vicky')
stu1.extend('tina')
lst=['rocky','drake']
stu1.append(lst)
stu1.extend(lst)
stu1.insert(12,'bob')
#stu1.clear()
print(stu1)
print(stu1.pop(5))
print(stu1)"""

"""alist=[10,20,30,40,30,50,30,50,30]
#print(alist.pop(0))
print(alist)
alist.remove(20)
print(alist)
while 30 in alist:
    alist.remove(30)
print(alist)
print(alist.index(50,1,6))
print(alist)"""

"""str="hello world"
print(str[0],str[-1],str[-2])
print(str[0:7])"""

"""name1='anand'
name2='john'
duration=10
str=name1+ " and " +name2+ " are friends for " +str(duration)+ " years"
print(str)

tpl =()
print(type(tpl), len(tpl))

Major=('physics','chemistry','mathematics','computer science','music')
print(type(Major))
print(Major)
del Major
print(Major)"""

"""set_a = {10, 20, 30, 40, 50, 30, 30, 30}
for x in set_a:
    print(x)"""

"""setA={'c','x','d','b','p','a'}
setB={'d','p','z'}
setA.difference_update(setB)
print(setA)
#print(setA-setB)"""

stu={'john':6.66,'ket':4.45,'raj':18.69}
print(stu['raj'])
stu['raj']=stu['raj']+1
print(stu['raj'])
for k in stu:
    print(k, '_', stu[k])
stu['peter']=9.98
print(stu)
