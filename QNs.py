import numpy as np
x=10
y=3
print(x+y)
print(x*y)
print(x/y)
print(np.sin(x))
print(8*np.sin(x))
print(x**y)

s="123"
N=float(s)
print(N)
print(type(s), type(N))

str1="HELLO"
str2="hello"
print(str1 == str2)
print(str1.lower() == str2)

str3="Python"
str4="Python is great!"

if str3 in str4:
    print("True")
else:
    print("False")

dict1={1:"Python",
      2:"is",
      3:"great",
      4:"!"}

print(dict1.keys())
print(dict1.values())
print(dict1[3])

list1=[1,8,9,15]
list1.insert(1,2)
print(list1)
list1.append(4)
print(list1)

tuple1=("One")
print(tuple1)
tuple2=tuple1,1
print(tuple2)

list2=[2,3,2,3,1,2]
set1=set(list2)
print(set1)
set2={2,3,2}
print(set2.union(set2))
print(set2.intersection(set2))
print(set2.difference(set2))

arr1=np.array([1,4,3,2,9,4])
arr2=np.array([2,3,4,1,2,3])
print(arr1 > arr2)

arr3=np.linspace(0,100,100)
print(arr3)

arr4=np.array([[3,5,3],[2,2,5],[3,8,9]])
print(arr4.T)

arr5=np.zeros((2,4))
print(arr5)
arr5[0,1]=1
arr5[1,1]=1
print(arr5)
