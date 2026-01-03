import numpy as np

def my_sinhx(x):
    y=(np.exp(x)-np.exp(-x))/2
    return y

x,y,z=0,1,2
print(my_sinhx(x))
print(my_sinhx(y))
print(my_sinhx(z))

traingleArea=lambda b,h:(b*h)/2

b,h=2,3
print(f"The area of the traingle where breadth is {b} and height is {h} is {traingleArea(b,h)}")

#My implementation
def splitMatrix(m):
    print(f"The size dimension(shape) of the matrix is {m.shape}")
    print(type(m.shape))
    list1=list(m.shape)
    print(list1[1]) # represents the column of the matrix to determine whether it is odd or even
    print(type(list1[1]))
    print(f"The value of the column is {list1[1]}")
    slicer=list1[1]
    if slicer%2 == 0:
        print(f"The number is divisible by 2")
        print("Entered the if  statement block")
        sliceVar1=list1[1]//2 - 1  
        sliceVar2=list1[1]//2 
        sliceVar3=list1[1]-1
        print(f"The value of sliceVar1 is {sliceVar1}")
        print(type(sliceVar2))
        print(f"The value of sliceVar2 is {sliceVar2}")
        m1=m[:,[0,sliceVar1]]
        m2=m[:,[sliceVar2,sliceVar3]]
    else:
        print(f"The number is not divisible by 2")
        print("Entered the else statement block")
        sliceVar=[]
        for i in range(list1[1]-1):
            sliceVar.append(i)

        for i in range(list1[1]//2 + 1 ):
            print(f"First for loop {i}")
            m1=m[:,[0,sliceVar[i]]]
    

        i=list1[1]//2 + 1
        for i in range(list1[1]-1):
            print(f"Second for loop {i}")
            m2=m[:,[sliceVar[i]]]
                
    
    return [m1,m2]

#Google Gemini Implementation 
def splitMatrix(m):
    cols=m.shape[1] # get the no of columns in the matrix
    mid=(cols+1)//2

    m1=m[:,:mid]
    m2=m[:,mid:]
    return [m1,m2]


m=np.array([[1,2,3],[4,5,6],[7,8,9]])
#m=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
m=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(m)
list1=splitMatrix(m)
print(list1[0])
print(list1[1])

def my_cylinder(r,h):
    s=2*np.pi*r**2 + 2*np.pi*r*h
    h=np.pi*r**2*h
    return list[s,h]


r,h=1,5
print(my_cylinder(r,h))


def my_n_odds(n):
    counter=0
    i=0
    for i in (n):
        if(i%2 != 0):
            counter=counter+1

    return counter

arr=np.arange(0,100,1)
print(arr)
print(arr.shape[0])
print(f"The number of odd numbers in the array is {my_n_odds(arr)}")


def my_twos(m,n):
    arr1=np.ones((m,n))
    arr2=np.ones((m,n))
    return arr1+arr2
m,n=3,2
print(my_twos(m,n))

difference = lambda x,y:x-y

print(difference(2,1))

def add_strings(a,b):
    return (a+b)

str1=add_strings("Programming"," ")
str2=add_strings("is"," fun")
print(add_strings(str1,str2))

def my_donut_area(n,m):
    area=np.pi*(m**2 -n**2)
    return area

a=np.arange(1,4)
b=np.arange(2,7,2)
print(a)
print(b)
print(my_donut_area(a,b))

def my_within_tolerance(A,a,tol):
    diff=np.abs(A-a)
    return diff[diff < tol].tolist()
    

A=np.array([0,1,2,3])
a=1.5
tol=0.75
print(my_within_tolerance(A,a,tol))

def bounding_array(A,top,bottom):
    A[A < bottom] = bottom
    A[A > top] = top
    return A

A=np.arange(-5,6,1)
top,bottom=3,-3
print(A)
print(bounding_array(A,top,bottom))

greetings =lambda name,age : f"Hi my name is {name} and I am {age} years old"

print(greetings("John",26))
