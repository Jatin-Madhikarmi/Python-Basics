import numpy as np
x=np.array([1,2,3])
print(x)
print(f"The first element of the matrix x is {x[0]}")
print(f"The last element of the matrix x is {x[-1]}")

y=np.array([[1,2,3],[4,5,6]])
print(y)
print(y.shape) #prints the dimension of the matrix
print(y.size) #prints the no of elements in the matrix

z=np.arange(0,200,5)
print(z)
print(type(z))

print(np.arange(0.5,3,0.5))

print(np.linspace(3,9,5))


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[:,[0,1,2]])

b=np.identity(3)
print(b)

c=np.empty(3)
print(c)

d=np.arange(1,7)
print(f"Before indexing is {d}")
d[0:3]=7
print(f"After indexing is {d}")

e=np.zeros((2,2))
print(f"Before the array indexing {e}")
e[0,0]=1
e[0,1]=2
e[1,0]=3
e[1,1]=4
print(f"After the array indexing {e}")

print(e**2) # exponential i.e power raised to 2

f=np.array([[1,2],[3,4]])
print(e+f)
print(np.sqrt(f))
print(f>=3)
g=f[f>1]
print(g)
g[g>3]=3
print(g)
print(f.T)

print("Using the indentity")
array=np.identity(4)
print(array)

arr=np.array([1,2,3])
list1=[1,2,1]
diff=[]
diff=arr-list1
print(diff)
print(type(diff))

two_2d_arr=np.array([[1,2],[3,4]])
print(two_2d_arr)
print(two_2d_arr[0])
print(two_2d_arr[1])
print(type(two_2d_arr[0]))

list2=[4,3]
arr=np.array([1,2])
for i in range(2):
    if arr.all() >= two_2d_arr[i].all():
        print("Yes the list is bigger")
    else:
        print("No the list is not bigger")

arr1=np.array([1,2,3])
arr2=np.array([1,2,4])

if (arr1 == arr2).all():
    print("Both the arrays are equal.\n")
else:
    print("Both the array's are not equal.\n")


arr1=np.arange(1,50,10) 
# Here the arange function is takes a start and stop with the interval, i.e we give the start value and the ending value and the interval
# between those values that are to be generated. It is not necessary that the last element will be equal to the ending value that we provided
# so it generates the array on the basis of the start,end and the interval which are to be provided i.e in this case we provided the 
# interval value to be 10 so there is a spacing of 10 between the values generated.
arr2=np.linspace(1,50,10)
#* Here the linspace function takes the start value,end value and the total number of elements are to be in the array,i.e the start and 
# ene values are exactly the same the third argument is the number of elements in our array. So this function's job is to generated exactly
# the numbers of elements based on the third argument and the start and end values.*#
print(f"The value of the array arr1 is {arr1}")
print(f"The value of the array arr2 is {arr2}")